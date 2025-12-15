# 📊 Advanced Analytics & Machine Learning  
### End-to-End Commercial Insight Pipeline for 3PL Shipping Data

This folder contains a **five-notebook advanced analytics sequence** demonstrating how shipment- and charge-level logistics data can be transformed into **commercial insight, risk detection, and AI-assisted decision support**.

The notebooks progress from **data certification** through **statistical analysis** and into **machine learning and AI-assisted narrative generation**, reflecting how modern analytics teams operate in production finance and operations environments.

All analysis is grounded in realistic 3PL business logic: pricing, margin protection, loss-making detection, and charge behaviour.

---

## 🎯 What This Segment Demonstrates

Across Notebooks **01 → 05**, this project demonstrates the ability to:

- Validate and certify analytics-ready datasets
- Apply disciplined data quality and reconciliation checks
- Engineer commercial features from raw shipment and charge data
- Detect outliers using statistical techniques
- Identify behavioural patterns in pricing and cost structures
- Apply clustering to segment clients and suppliers
- Combine classical analytics with LLM-based narrative insight
- Translate data into **commercially actionable recommendations**

This is **not** a toy ML project — it reflects real-world analytics decision-making.

---

## 🧭 Notebook Overview

### **Notebook 01 — Data Ingestion, Validation & Quality Profiling**
**Foundation & Certification Layer**

- Controlled ingestion of shipment and charge fact tables
- Schema validation and drift detection
- Primary key and referential integrity checks
- Null profiling and cardinality analysis
- Margin and loss-flag business rule validation
- Charge-to-shipment reconciliation diagnostics
- Dataset certification for downstream modelling

> Purpose: establish **trust** in the data before any modelling occurs.

---

### **Notebook 02 — Feature Engineering & Commercial Enrichment**
**Analytics-Ready Feature Layer**

- Shipment- and client-level aggregations
- Margin %, loss rates, and volume metrics
- Charge mix and behavioural indicators
- Normalisation and scaling preparation
- Feature sets designed explicitly for modelling

> Purpose: transform validated data into **model-ready commercial signals**.

---

### **Notebook 03 — Outlier Detection & Statistical Anomaly Detection**
**Risk & Exception Identification**

- Univariate and multivariate outlier detection
- Distribution-based thresholding
- Identification of extreme margin, cost, and pricing behaviours
- Separation of statistical anomalies from legitimate edge cases
- Business interpretation of outlier drivers

> Purpose: surface **hidden financial risk and unusual behaviour**.  
> :contentReference[oaicite:0]{index=0}

---

### **Notebook 04 — Price–Cost Pattern Mining & Charge Behaviour**
**Behavioural & Structural Analysis**

- Price vs cost relationship analysis
- Charge-level margin contribution profiling
- Identification of structurally loss-making charge types
- Pattern mining across services, destinations, and clients
- Evidence for pricing and routing reviews

> Purpose: understand **why margins behave the way they do**, not just where.

---

### **Notebook 05 — AI-Assisted Segmentation & Narrative Margin Insights**
**Machine Learning + AI Decision Support**

- Client and supplier clustering using behavioural features
- Interpretation of clusters using commercial metrics
- Automated plain-English profiles for each segment
- AI-generated commercial recommendations
- Example use cases: price review, routing changes, client conversations

> Purpose: demonstrate how **traditional analytics and modern LLMs work together**.

---

## 🧠 Design Philosophy

This segment is intentionally structured to reflect **production analytics thinking**:

- No blind trust in source data  
- Explicit validation before modelling  
- Business logic embedded throughout  
- AI used to *augment*, not replace, analysis  
- Clear separation between data, features, models, and narrative  

Each notebook builds on the last — skipping steps would introduce risk.

---

## 🧰 Tools & Technologies

| Layer | Tools |
|-----|------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Storage | Parquet |
| Statistics | SciPy, custom statistical logic |
| Machine Learning | scikit-learn |
| AI Integration | OpenAI API (optional, post-billing) |
| Environment | Conda, Jupyter |
| Visualisation | Matplotlib / Seaborn (selective use) |

---

## 📂 Data Model Assumptions

The analysis assumes two core fact tables:

### Shipment Fact Table
- One row per shipment
- Commercial totals (sales, costs, margin)
- Client, supplier, service, destination attributes

### Charge Fact Table
- Multiple rows per shipment
- Individual charge types
- Sales and cost attribution per charge

The notebooks are designed to scale to **millions of rows** with minimal refactoring.

---

## 📈 Why This Matters

This portfolio segment demonstrates readiness for:

- Finance analytics roles
- Commercial performance analysis
- Pricing and margin optimisation
- Advanced Power BI / analytics engineering workflows
- Data science roles grounded in real business problems

It shows not just *how to analyse data*, but **how to think like a commercial analytics professional**.

---

## 🧑‍💼 Author

**Lewis Andrews**  
Advanced Analytics • Finance • Logistics  
Python • Power BI • DuckDB / dbt  

