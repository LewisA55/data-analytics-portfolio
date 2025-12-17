from __future__ import annotations

import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import yaml


def load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def require_columns(df: pd.DataFrame, required: List[str], name: str) -> None:
    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"[{name}] Missing required columns: {missing}")


def expected_cost(weight: float, base_weight: float, base_cost: float, extra_weight: float, extra_rate: float) -> float:
    """
    Generic stepped rate calculation:
    - up to base_weight => base_cost
    - above base_weight => base_cost + ceil((weight-base_weight)/extra_weight) * extra_rate
    """
    if pd.isna(weight) or pd.isna(base_weight) or pd.isna(base_cost) or pd.isna(extra_weight) or pd.isna(extra_rate):
        return np.nan

    if weight <= base_weight:
        return float(base_cost)

    units = math.ceil((weight - base_weight) / extra_weight)
    return float(base_cost + units * extra_rate)


def reconcile(invoice_df: pd.DataFrame, rate_df: pd.DataFrame, cfg: dict) -> Tuple[pd.DataFrame, pd.DataFrame]:
    # --- Config ---
    match_keys = cfg["keys"]["rate_match_keys"]
    group_key = cfg["keys"]["invoice_group"]
    tol_abs = float(cfg["tolerances"]["amount_abs"])

    inv_cols = cfg["columns"]["invoice"]
    rate_cols = cfg["columns"]["rate_card"]

    # --- Schema checks ---
    require_columns(invoice_df, list(inv_cols.values()), "invoice")
    require_columns(rate_df, list(rate_cols.values()), "rate_card")

    # --- Standardise column names (internal canonical names) ---
    invoice = invoice_df.rename(columns={v: k for k, v in inv_cols.items()}).copy()
    rates = rate_df.rename(columns={v: k for k, v in rate_cols.items()}).copy()

    # --- Join validation: many invoice rows to one rate row ---
    merged = invoice.merge(
        rates,
        on=match_keys,
        how="left",
        validate="m:1"
    )

    # --- Expected amount calculation ---
    merged["expected_amount"] = merged.apply(
        lambda r: expected_cost(
            r["billed_weight"],
            r["base_weight"],
            r["base_cost"],
            r["extra_weight"],
            r["extra_rate"],
        ),
        axis=1
    )

    # --- Variance ---
    merged["variance"] = merged["billed_amount"] - merged["expected_amount"]
    merged["variance_pct"] = np.where(
        merged["expected_amount"].notna() & (merged["expected_amount"] != 0),
        merged["variance"] / merged["expected_amount"],
        np.nan
    )

    # --- Control flags / statuses ---
    merged["rate_found"] = merged["expected_amount"].notna()

    merged["status"] = np.select(
        [
            ~merged["rate_found"],
            merged["variance"].abs() <= tol_abs,
            merged["variance"] > tol_abs,
            merged["variance"] < -tol_abs,
        ],
        [
            "NO_RATE_FOUND",
            "MATCH",
            "OVERCHARGED",
            "UNDERCHARGED",
        ],
        default="REVIEW"
    )

    # --- Summary output ---
    summary = (
        merged.groupby(group_key, as_index=False)
        .agg(
            consignments=("tracking_id", "nunique"),
            billed_total=("billed_amount", "sum"),
            expected_total=("expected_amount", "sum"),
            variance_total=("variance", "sum"),
            overcharged=("status", lambda s: int((s == "OVERCHARGED").sum())),
            undercharged=("status", lambda s: int((s == "UNDERCHARGED").sum())),
            missing_rate=("status", lambda s: int((s == "NO_RATE_FOUND").sum())),
        )
    )

    summary["variance_pct"] = np.where(
        summary["expected_total"] != 0,
        summary["variance_total"] / summary["expected_total"],
        np.nan
    )

    return merged, summary


def main():
    root = Path(__file__).resolve().parent

    cfg = load_yaml(root / "config.yaml")

    invoice_path = root / "sample_input" / "invoice_sample.csv"
    rate_path = root / "sample_input" / "rate_card_sample.csv"

    out_dir = root / "sample_output"
    out_dir.mkdir(exist_ok=True)

    invoice_df = pd.read_csv(invoice_path)
    rate_df = pd.read_csv(rate_path)

    detail, summary = reconcile(invoice_df, rate_df, cfg)

    detail.to_csv(out_dir / cfg["output"]["detail_file"], index=False)
    summary.to_csv(out_dir / cfg["output"]["summary_file"], index=False)


if __name__ == "__main__":
    main()