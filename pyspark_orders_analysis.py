from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, month, year

spark = SparkSession.builder.appName("OrdersETL").getOrCreate()

df = spark.read.csv("Orders.csv", header=True, inferSchema=True)

df = df.withColumn("Date", col("Date").cast("date")) \
       .withColumn("Units Sold", col("Units Sold").cast("int")) \
       .withColumn("Revenue", col("Revenue").cast("double")) \
       .withColumn("Cost", col("Cost").cast("double"))

df.createOrReplaceTempView("Orders")

sales_summary = spark.sql("""
    SELECT Product, SUM(Revenue) AS TotalRevenue, SUM(Cost) AS TotalCost
    FROM Orders
    GROUP BY Product
    ORDER BY TotalRevenue DESC
""")

best_sellers = spark.sql("""
    SELECT Product, COUNT(*) AS TotalOrders, SUM(Units Sold) AS TotalUnitsSold
    FROM Orders
    GROUP BY Product
    ORDER BY TotalUnitsSold DESC
    LIMIT 10
""")

monthly_sales = spark.sql("""
    SELECT MONTH(Date) AS Month, SUM(Revenue) AS MonthlyRevenue
    FROM Orders
    WHERE YEAR(Date) = 2020
    GROUP BY Month
    ORDER BY Month
""")

duplicates = spark.sql("""
    SELECT OrderID, COUNT(*) 
    FROM Orders
    GROUP BY OrderID
    HAVING COUNT(*) > 1
""")

missing_data = spark.sql("""
    SELECT * FROM Orders
    WHERE OrderID IS NULL 
    OR CustomerID IS NULL 
    OR Product IS NULL 
    OR Date IS NULL
""")

sales_summary.show()
best_sellers.show()
monthly_sales.show()
duplicates.show()
missing_data.show()

spark.stop()
