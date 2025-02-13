# Super Store Profit Analysis

## Project Overview
This project analyzes sales and profit data from a Super Store using SQL, PySpark, and Python. The goal is to extract, transform, and load (ETL) data, then generate insights on sales trends, best-selling products, and profit analysis.

## Technologies Used
- Python (Pandas, SQLite, Matplotlib)
- PySpark (Data Processing)
- SQL (Data Transformation & Querying)
- Power BI (Visualization)

## Files & Directories
- Orders.csv - Dataset containing sales records.
- orders_analysis.sql - SQL queries for analysis.
- pyspark_orders_analysis.py - PySpark script for data processing.
- Super Store Report.pbix - Power BI report for visualization.
- README.md - Project documentation.

## Setup & Installation
1. Clone the repository:
   ```sh
   git clone <https://github.com/SatwikaKadiyala/Super-Store-Profit->
   ```
2. Install dependencies:
   ```sh
   pip install pandas pyspark sqlite3
   ```
3. Run the SQL queries:
   ```sh
   sqlite3 orders_db.sqlite < orders_analysis.sql
   ```
4. Run the PySpark script:
   ```sh
   python pyspark_orders_analysis.py
   ```
5. Open `Super Store Report.pbix` in Power BI for insights.

## Future Enhancements
- Implement machine learning models for demand forecasting.
- Automate data pipeline with Apache Airflow.
- Deploy a web dashboard for real-time monitoring.

## Author
Lakshmi Sai Satwika Kadiyala

