# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.customerId
WHERE customerId IS NULL;