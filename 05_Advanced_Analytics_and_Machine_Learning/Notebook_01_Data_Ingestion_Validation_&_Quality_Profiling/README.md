# 📦 Data Ingestion, Validation & Quality Profiling  
### Analytics Data Certification for 3PL Shipping Data

This notebook forms the **foundation** of a multi-notebook analytics portfolio focused on logistics, pricing, and margin analysis in a 3PL environment.

Although the source datasets are already analytics-ready, this notebook provides a **formal ingestion, validation, and quality certification layer** to ensure the data is trustworthy before downstream feature engineering, modelling, and AI-driven insights.

It reflects how mature analytics teams operate in production environments:  
**no assumptions, explicit checks, documented risks.**

---

## 🎯 Purpose of This Notebook

This notebook acts as a **quality gate** for all downstream analysis (Notebooks 02–05).

Its objectives are to:

- Ingest analytics-ready shipment and charge fact tables in a controlled manner  
- Validate schema, keys, and referential integrity  
- Profile data quality (nulls, distributions, cardinality)  
- Validate core business logic (margin and loss flags)  
- Document outliers and reconciliation behaviour  
- Certify the dataset for modelling and AI use  

No destructive cleaning is performed.

---

## 🧠 Why This Step Matters

In real-world finance and logistics analytics:

- Even “clean” data must be validated  
- Upstream pipelines can drift silently  
- Modelling without certification creates risk  
- Stakeholders need confidence in numbers  

This notebook demonstrates **engineering discipline**, not just analysis.

---

## 🧰 Technologies Used

| Layer | Tools |
|-----|------|
| Data Processing | Python, Pandas, NumPy |
| Storage Format | Parquet |
| Validation Logic | Schema checks, key integrity, rule-based validation |
| Environment | Conda, Jupyter Notebook |

---

## 📄 Data Inputs

### Shipment Fact Table  
**`fct_shipments_randomised.parquet`**

Shipment-level data including:
- `unique_tracking` (primary key)
- Booking date
- Client and supplier codes
- Destination country
- Service
- Total sales and total costs
- Loss-making flag

### Charge Fact Table  
**`fct_charges_randomised.parquet`**

Charge-line-level data including:
- `unique_tracking` (foreign key)
- `charge_type`
- `sales_amount`
- `cost_amount`

---

## 📄 Notebook Structure

### **1. Setup & Configuration**
- Environment setup
- Path configuration
- Display and formatting settings

### **2. Controlled Data Ingestion**
- Explicit ingestion from parquet
- Row counts logged for reproducibility

### **3. Schema Validation**
- Required column checks
- Detection of schema drift
- Clear signalling of upstream changes

### **4. Key & Referential Integrity**
- Primary key uniqueness validation
- Orphan charge detection

### **5. Data Quality Profiling**
- Null-rate analysis
- Cardinality profiling
- Numeric distribution summaries

### **6. Business Rule Validation**
- Margin calculation consistency
- Loss-making flag validation
- Financial sanity checks

### **7. Outlier Awareness**
- Identification of extreme cost and margin cases
- No automatic removal (documented only)

### **8. Charge Roll-Up Reconciliation**
- Aggregation of charge lines to shipment level
- Comparison against shipment totals
- Documentation of reconciliation differences

### **9. Data Certification Summary**
- Pass / Fail / Review status for each check
- Clear readiness signal for downstream notebooks

### **10. Conclusion & Handover**
- Dataset certified for enrichment, modelling, and AI analysis

---

## 📊 Outputs

- Data quality profile tables  
- Reconciliation diagnostics  
- Outlier inspection tables  
- Final certification summary  

These outputs provide transparency and confidence in the dataset.

---

## 🔗 Downstream Dependencies

This notebook directly supports:

- **Notebook 02 — Feature Engineering & Enrichment**
- **Notebook 04 — Price/Cost Pattern Mining & Charge Behaviour**
- **Notebook 05 — AI-Assisted Segmentation & Narrative Margin Insights**

All downstream notebooks assume this validation step has been completed.

---

## 📈 Why This Project Matters

This notebook demonstrates the ability to:

- Treat analytics-ready data with professional rigour  
- Validate upstream pipelines rather than blindly trusting them  
- Apply business logic checks grounded in domain knowledge  
- Build analytics workflows that scale beyond ad-hoc analysis  

It shows readiness for real-world analytics, finance, and data engineering roles.

---

## 🧑‍💼 Author

**Lewis Andrews**  
Advanced Analytics, Finance & Data Platforms  