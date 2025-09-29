# Shipping Margin Report (Power BI + SQL + Python)

## Overview
Designed a 12-page Power BI report analysing shipping performance and margin tracking 
for a logistics business (8M+ rows of data).  
The report provides insights for Finance, Commercial, and Operations teams, 
supporting supplier negotiations and identifying loss-making jobs.

## Key Features
- Executive dashboard with KPIs (Revenue, Cost, Margin %).  
- Drillthrough pages for country-level and supplier-level analysis.  
- Charge breakdown visuals (fuel surcharge recovery, returns, surcharges).  
- Benchmark scatter plots comparing clients and suppliers.  

## Tech Stack
- Power BI (DAX measures, 12-page interactive report).  
- SQL (fact tables for shipments and charges).  
- Python (CSV → Parquet → DuckDB pipeline).  
- dbt (enrichment and fiscal calendar modelling).
  
## 📂 Files
- [DAX Measures](Dax-Measures.md)  
- [Pipeline Overview](Pipeline_Overview.md)  
- [SQL Models](SQL-Models.sql)  
- [Report Screenshots](Report-Screenshots)  

## Sample Visuals
![Executive Dashboard]
![Supplier Spotlight]

## Impact
- Automated reporting for executives and the board management pack.  
- Reduced manual Excel-based reporting by ~20 hours/month.  
- Provided transparency into supplier-level margin performance.  
