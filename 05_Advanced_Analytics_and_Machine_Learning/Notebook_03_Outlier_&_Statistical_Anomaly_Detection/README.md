📘 Notebook 03 — Outlier Detection & Statistical Anomaly Detection
Advanced Analytics & Machine Learning for Logistics Finance

This notebook demonstrates a multi-method anomaly detection framework applied to 10 million enriched logistics shipment records.

It showcases techniques used in

audit & assurance

fraud detection

cost-control analytics

operational insight

risk identification

Objective

Detect and explain unusual shipment behaviours such as

Mispriced consignments

Unexpected cost spikes

Supplier-level pricing inconsistencies

Operational anomalies

Rate-card mismatches

Patterns not visible through standard BI tools

The goal is to demonstrate analytical depth, ML capability, and domain understanding.

Techniques Included

This notebook implements multiple anomaly-detection methods

1. Z-Score Outlier Detection

Simple statistical deviation

Useful for margin-based screening

2. IQR (Interquartile Range)

Robust against skew and long tails

Highlights cost irregularities

3. Isolation Forest (Unsupervised ML)

Tree-based anomaly scoring

Captures multivariate irregularities

4. Local Outlier Factor (Density-Based)

Detects anomalies in dense vs sparse regions

Effective for recognising unusual shipment profiles

5. Regression-Based Anomaly Detection

Predicts expected cost based on sales

Flags deviations from normal pricing relationships

6. PCA Projection (Dimensionality Reduction)

Visualises anomaly clusters

Useful for storytelling to stakeholders

Key Outputs

The notebook produces

• Ranked anomaly tables

(Z-score, IQR, Isolation Forest, LOF)

• PCA scatter plots

Colour-coded anomaly clusters

• Regression residual analysis

Shows where cost ≠ expected cost

• Business insights

Supplierservice combinations driving irregularities

• Combined anomaly scoring

Multiple methods aggregated into a single anomaly index

Why This Notebook Matters

This project shows strong capability in

✔ Financial analytics
✔ Risk identification
✔ Machine learning
✔ Data storytelling
✔ Domain understanding (logisticscost models)
✔ Reproducible analysis
✔ High-volume data handling

It is designed specifically to strengthen applications for

Audit apprenticeships

Data analytics roles

Risk & assurance positions

Consulting and operations analytics

How to Run
Requirements

Python 3.9+

VS Code + Jupyter extension

Packages in requirements.txt

Run
pip install -r requirements.txt
jupyter notebook


Open the file

Notebook_03_Outlier_Detection.ipynb

Included Files
03_Outlier_Detection
│
├── Notebook_03_Outlier_Detection.ipynb   -- Full notebook with code
├── Notebook_03_Outlier_Detection.html    -- Clean rendered report
├── README.md                             -- This file
├── requirements.txt
└── sample_outputs
      ├── pca_scatter.png
      ├── iso_forest_scores.png
      └── anomaly_table.png

Summary

The notebook identifies multiple categories of anomalies, including

Pricing patterns inconsistent with supplier rate-cards

Margin outliers affecting revenue and cost accuracy

Supplierservice outlier clusters

Operational mischarges (heavy underover cost)

Unexpected pricing relationships between sales + cost

It provides clear recommendations for

Billing corrections

Supplier performance review

Data quality improvement

Rate-card alignment

This demonstrates real-world commercial and analytical impact.