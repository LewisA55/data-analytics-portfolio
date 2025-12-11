# 📦 AI-Assisted Segmentation & Narrative Margin Insights  
### Advanced Analytics & Machine Learning for 3PL Shipping Data

This notebook is part of a broader analytics portfolio showcasing real-world data engineering, machine learning, and AI-driven insights in a logistics environment.  
It demonstrates how to engineer complex behavioural features, segment clients or suppliers using machine learning, and automatically generate high-quality commercial narratives using OpenAI’s API.

---

## 🚀 Project Overview

3PL businesses handle thousands of shipments per day, with costs driven by a mix of services, surcharges, client behaviour, and operational patterns.  
This notebook provides an end-to-end workflow to:

### 🔹 Build client- or supplier-level behavioural datasets
From shipment and charge-level transactional data, including:
- Margin %
- Loss rate
- Shipment volume
- Revenue and cost behaviour
- Charge mix usage (fuel, remote area, express etc.)

### 🔹 Segment customers using machine learning
Using **KMeans clustering**, the notebook identifies behavioural groups based on:
- Profitability
- Operational cost pressures
- Charge/fee utilisation patterns
- Shipment intensity and value

These segments reflect real commercial groupings such as:
- High-value / low-risk  
- High-volume / low-margin  
- Small revenue / high loss-rate  
- Volatile-margin clients  

### 🔹 Automatically generate narrative insights (AI-Powered)
With OpenAI’s Responses API, the notebook produces:
- Plain-English summaries of each cluster  
- Commercial recommendations  
- Pricing and margin-protection actions  
- Executive-ready bullet points  
- Supplier/client behaviour explanations  

> 💡 *If no API credits are available, AI cells gracefully skip execution.*

---

## 🧰 Technologies Used

| Layer | Tools |
|------|-------|
| Data Processing | Python, Pandas, NumPy |
| Machine Learning | scikit-learn (KMeans, StandardScaler) |
| Visualisation | Seaborn, Matplotlib |
| AI Narratives | OpenAI Responses API |
| Environment | Conda (isolated environment), Jupyter Notebooks |

---

## 📄 Notebook Structure

### **1. Setup & Configuration**
Environment setup, imports, and optional OpenAI API initialisation.

### **2. Load Shipment & Charge Fact Tables**
Reads parquet datasets that represent real 3PL transactional shipping data.

### **3. Feature Engineering**
Builds client-level performance metrics including:
- Margin %
- Loss rate
- Shipment volume
- Charge usage patterns

### **4. Clustering Model**
Standardises features and applies KMeans segmentation to group behavioural profiles.

### **5. Cluster Summaries**
Generates easy-to-read summary tables for each segment.

### **6. AI-Generated Narratives (Optional)**
Uses OpenAI’s API to produce:
- Cluster explanations
- Operational insights
- Pricing recommendations
- Executive summaries

### **7. Conclusions**
Connects ML and AI insights to real commercial decision-making in logistics.

---

## 📦 Project Files
