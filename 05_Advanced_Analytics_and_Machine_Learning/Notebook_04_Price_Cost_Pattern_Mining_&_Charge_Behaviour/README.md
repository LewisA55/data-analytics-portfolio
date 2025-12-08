# 📦 Price/Cost Pattern Mining & Charge Behaviour  
### Advanced Analytics for 3PL Margin Performance

This notebook is part of a wider analytics portfolio built to demonstrate how data engineering, statistical modelling, and commercial analysis can be combined to understand and improve shipping margin performance in a 3PL environment.

It focuses on **charge-level behaviour**, analysing how fuel, remote area fees, express surcharges, and other cost drivers influence margin, loss rate, and supplier performance.

---

## 🚀 Project Overview

Shipping cost behaviour is influenced heavily by the presence, frequency, and pricing of additional charges.  
This notebook explores how those charges impact profitability and operational patterns through:

### 🔹 Price/Cost pattern mining  
Identifies which charges drive:

- Highest cost  
- Greatest revenue uplift  
- Highest/lowest margin  
- Largest contribution to loss-making shipments  

### 🔹 Loss uplift analysis  
For each charge type:

- Compute loss rate for shipments with the charge  
- Compare against the **baseline loss rate**  
- Quantify uplift (percentage-point impact)  
- Plot frequency vs uplift (log scale)

This reveals which charges are **high-risk**, **low-risk**, or **neutral**.

### 🔹 Supplier × charge matrix  
Creates a **Supplier × Charge heatmap**, highlighting:

- Which suppliers apply certain surcharges more frequently  
- Which combinations systematically erode margin  
- Supplier behaviours worth challenging or renegotiating

### 🔹 Logistic regression modelling  
A predictive model is trained to estimate whether a shipment becomes loss-making based on charge presence.  
This includes:

- One-hot encoding of charges  
- Logistic regression fit  
- Odds ratios for interpretability  
- Identification of:
  - **Risk-increasing charges**  
  - **Protective charges**  
  - **Unexpected interactions**  

### 🔹 Business interpretation  
Provides narrative insights into:

- Where margin leakage occurs  
- Which charges require review  
- Which clients/suppliers over-index on risky fees  
- Operational and commercial opportunities

---

## 🧰 Technologies Used

| Layer | Tools |
|------|-------|
| Data Processing | Python, Pandas, NumPy |
| Visualisation | Seaborn, Matplotlib |
| Modelling | scikit-learn (LogisticRegression) |
| Business Analytics | Uplift analysis, risk scoring, marginal impact analysis |
| Environment | Conda, Jupyter Notebooks |

---

## 📄 Notebook Structure

### **1. Load & Join Shipment + Charge Facts**
- Reads `fct_shipments_randomised.parquet`
- Reads `fct_charges_randomised.parquet`
- Builds a combined shipment-level analytical table

### **2. Exploratory Charge Analytics**
- Revenue, cost, and margin by charge type  
- Distribution patterns  
- Frequency and spend patterns

### **3. Loss Uplift Analysis**
- Calculates baseline loss rate  
- Computes uplift per charge  
- Generates frequency vs uplift scatterplots  
- Identifies high-frequency/high-risk charges

### **4. Supplier–Charge Interaction**
- Builds a Supplier × Charge matrix  
- Highlights margin patterns  
- Creates heatmaps for comparison

### **5. Predictive Modelling (Logistic Regression)**
- Creates binary charge indicators  
- Fits logistic regression  
- Computes odds ratios  
- Sorts charges into:
  - Risk amplifiers  
  - Neutral drivers  
  - Protective factors  

### **6. Narrative Insights**
Summaries include:
- Key charges responsible for margin erosion  
- Supplier behaviours and anomalies  
- Commercial recommendations (pricing, routing, minimums)  
- Validation suggestions for Finance/AP/Carrier Management teams

---

## 📊 Example Outputs

- **Charge vs Loss Uplift Plot** (log-scale frequency)  
- **Supplier × Charge Heatmap**  
- **Odds Ratio Chart** (high-risk vs protective charges)  
- **Sorted charge ranking tables**

These visuals provide a clear story for commercial teams without needing deep statistical knowledge.

---

## 📈 Why This Project Matters

This notebook demonstrates capability across:

- Practical **data engineering**  
- Commercial **margin analytics**  
- Applied **statistical modelling**  
- Real **3PL domain understanding**  
- Clear **stakeholder storytelling**

It shows how advanced analytics can uncover:

- Hidden margin leakage  
- Poorly priced surcharges  
- Supplier overcharges  
- Client behaviours driving cost  
- Opportunities to protect profitability  

Perfect for illustrating end-to-end thinking:  
**Data → Insight → Explanation → Business Action**

---

## 🧑‍💼 Author

**Lewis Andrews**  
Advanced Analytics, Finance & Data Platforms  
Logistics / 3PL • Python • Power BI • DuckDB/dbt  

