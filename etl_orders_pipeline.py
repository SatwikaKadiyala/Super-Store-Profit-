import pandas as pd
import sqlite3  

df = pd.read_csv("Orders.csv")  

df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%m-%d-%Y')
df['Quantity'] = df['Quantity'].replace(',', '', regex=True).astype(int)
df['TotalPrice'] = df['TotalPrice'].replace(',', '', regex=True).astype(float)
df['Profit'] = df['Profit'].replace(',', '', regex=True).astype(float)

conn = sqlite3.connect("orders_db.sqlite")  
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER,
        CustomerID INTEGER,
        ProductName TEXT,
        Quantity INTEGER,
        OrderDate DATE,
        TotalPrice REAL,
        Profit REAL
    )
""")

df.to_sql("Orders", conn, if_exists="replace", index=False)

query_sales = """
    SELECT ProductName, SUM(TotalPrice) AS TotalSales, SUM(Profit) AS TotalProfit
    FROM Orders
    GROUP BY ProductName
    ORDER BY TotalSales DESC;
"""
sales_summary = pd.read_sql(query_sales, conn)

query_best_sellers = """
    SELECT ProductName, COUNT(*) AS TotalOrders, SUM(Quantity) AS TotalQuantitySold
    FROM Orders
    GROUP BY ProductName
    ORDER BY TotalQuantitySold DESC
    LIMIT 10;
"""
best_sellers = pd.read_sql(query_best_sellers, conn)

query_monthly_sales = """
    SELECT strftime('%m', OrderDate) AS Month, SUM(TotalPrice) AS MonthlySales
    FROM Orders
    WHERE strftime('%Y', OrderDate) = '2020'
    GROUP BY Month
    ORDER BY Month;
"""
monthly_sales = pd.read_sql(query_monthly_sales, conn)

query_duplicates = """
    SELECT OrderID, COUNT(*) 
    FROM Orders
    GROUP BY OrderID
    HAVING COUNT(*) > 1;
"""
duplicates = pd.read_sql(query_duplicates, conn)

query_missing_data = """
    SELECT * FROM Orders
    WHERE OrderID IS NULL 
    OR CustomerID IS NULL 
    OR ProductName IS NULL 
    OR OrderDate IS NULL;
"""
missing_data = pd.read_sql(query_missing_data, conn)

conn.close()

print("✅ Sales Summary:\n", sales_summary.head())
print("\n✅ Best-Selling Products:\n", best_sellers.head())
print("\n✅ Monthly Sales Trends:\n", monthly_sales.head())
print("\n⚠️ Duplicate Orders (if any):\n", duplicates)
print("\n⚠️ Missing Data (if any):\n", missing_data)
