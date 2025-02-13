CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    ProductName VARCHAR(255),
    Quantity INT,
    OrderDate DATE,
    TotalPrice DECIMAL(10,2),
    Profit DECIMAL(10,2)
);

SELECT * FROM Orders
WHERE YEAR(OrderDate) = 2020;

SELECT * FROM Orders
WHERE ProductName = 'Chocolate Chip';

SELECT 
    ProductName, 
    SUM(TotalPrice) AS TotalSales, 
    SUM(Profit) AS TotalProfit
FROM Orders
GROUP BY ProductName
ORDER BY TotalSales DESC;

SELECT 
    ProductName, 
    COUNT(*) AS TotalOrders, 
    SUM(Quantity) AS TotalQuantitySold
FROM Orders
GROUP BY ProductName
ORDER BY TotalQuantitySold DESC
LIMIT 10;

SELECT 
    MONTH(OrderDate) AS Month, 
    SUM(TotalPrice) AS MonthlySales
FROM Orders
WHERE YEAR(OrderDate) = 2020
GROUP BY MONTH(OrderDate)
ORDER BY Month;

CREATE TABLE SalesSummary (
    ProductName VARCHAR(255),
    TotalSales DECIMAL(12,2),
    TotalProfit DECIMAL(12,2)
);

INSERT INTO SalesSummary (ProductName, TotalSales, TotalProfit)
SELECT 
    ProductName, 
    SUM(TotalPrice) AS TotalSales, 
    SUM(Profit) AS TotalProfit
FROM Orders
GROUP BY ProductName;

SELECT OrderID, COUNT(*) 
FROM Orders
GROUP BY OrderID
HAVING COUNT(*) > 1;

SELECT * FROM Orders
WHERE OrderID IS NULL 
   OR CustomerID IS NULL 
   OR ProductName IS NULL 
   OR OrderDate IS NULL;

SELECT 
    CustomerID, 
    SUM(TotalPrice) AS TotalSpent, 
    COUNT(OrderID) AS OrderCount
FROM Orders
GROUP BY CustomerID
ORDER BY TotalSpent DESC;

SELECT 
    ProductName, 
    COUNT(*) AS TotalOrders, 
    SUM(TotalPrice) AS RevenueGenerated
FROM Orders
GROUP BY ProductName
ORDER BY RevenueGenerated DESC;

SELECT 
    CustomerID, 
    SUM(TotalPrice) AS TotalRevenue
FROM Orders
GROUP BY CustomerID
ORDER BY TotalRevenue DESC
LIMIT 10;
