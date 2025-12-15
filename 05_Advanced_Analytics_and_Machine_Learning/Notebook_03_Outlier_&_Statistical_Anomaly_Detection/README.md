# 📘 Outlier Detection & Statistical Anomaly Detection  
### Advanced Analytics for Logistics Finance & Commercial Risk

This notebook presents a **multi-method anomaly detection framework** applied to a large, enriched logistics shipment dataset.  
The analysis is designed to identify **financial, pricing, and operational irregularities** that are not visible through standard reporting or dashboard-based analysis.

Rather than relying on a single statistical technique, the notebook combines **classical statistics, unsupervised machine learning, and regression-based diagnostics** to surface different categories of risk and unusual behaviour.

---

## 🎯 Analytical Objective

The objective of this analysis is to **detect, explain, and contextualise anomalous shipment behaviour**, including:

- Mispriced consignments  
- Unexpected cost spikes  
- Supplier-level pricing inconsistencies  
- Operational anomalies and mischarges  
- Rate-card misalignment  
- Non-linear pricing relationships between sales and cost  

The focus is not only on detection, but on **interpretability and commercial relevance**.

---

## 🧠 Analytical Philosophy

In complex pricing and cost environments, no single anomaly detection method is sufficient.  
Different techniques surface **different failure modes**, for example:

- Simple margin outliers  
- Dense-cluster deviations  
- Multivariate pricing breakdowns  
- Structural cost–revenue inconsistencies  

This notebook therefore applies **multiple complementary methods**, treating anomaly detection as an *investigative framework* rather than a binary flagging exercise.

---

## 🛠 Techniques Implemented

### **Z-Score Detection**
- Classical statistical deviation
- Effective for margin and cost screening
- Useful for rapid, explainable controls

### **Interquartile Range (IQR)**
- Robust to skewed and heavy-tailed distributions
- Highlights irregular cost behaviour
- Commonly used in financial assurance contexts

### **Isolation Forest (Unsupervised ML)**
- Tree-based anomaly scoring
- Captures complex, multivariate irregularities
- Scales well to high-volume data

### **Local Outlier Factor (LOF)**
- Density-based detection
- Identifies shipments that are anomalous relative to peer groups
- Effective for uncovering unusual operational profiles

### **Regression-Based Anomaly Detection**
- Models expected cost behaviour based on sales and shipment attributes
- Flags material deviations from expected pricing relationships
- Particularly useful for identifying pricing logic breakdowns

### **PCA Projection & Visualisation**
- Dimensionality reduction for complex feature spaces
- Visual clustering of anomalous behaviour
- Supports structured investigation and storytelling

---

## 📊 Key Outputs

The notebook produces:

- Ranked anomaly tables by method (Z-score, IQR, Isolation Forest, LOF)  
- Regression residual diagnostics highlighting cost vs expected cost divergence  
- PCA scatter plots illustrating anomaly clusters  
- Supplier × service insights identifying structural drivers of irregularity  
- A combined anomaly index aggregating signals across methods  

These outputs are designed to support **prioritisation, investigation, and decision-making**.

---

## 📈 Commercial & Analytical Value

This notebook demonstrates:

- Advanced statistical reasoning applied to real commercial data  
- Responsible use of unsupervised machine learning  
- Ability to handle large, high-dimensional datasets  
- Strong linkage between analytics and business interpretation  
- Clear separation between statistical anomalies and legitimate edge cases  

The analysis surfaces **actionable insight**, not just statistical noise.

---

## 🧾 Summary of Findings

The framework identifies multiple categories of anomalies, including:

- Pricing patterns inconsistent with supplier rate cards  
- Margin outliers impacting revenue and cost accuracy  
- Supplier–service combinations driving abnormal behaviour  
- Operational mischarges (material under- or over-costing)  
- Unexpected sales–cost relationships not captured by rule-based logic  

These findings naturally inform:
- Pricing and rate-card review  
- Supplier performance discussions  
- Billing correction and recovery  
- Data quality and process improvement  

---

## 🧑‍💼 Author

**Lewis Andrews**  
Advanced Analytics • Finance • Logistics  
Python • Machine Learning • Power BI • DuckDB/dbt  
