# Write your MySQL query statement below
SELECT CASE 
    WHEN (SELECT COUNT(DISTINCT salary) FROM Employee) < 2 THEN NULL 
    ELSE (
        SELECT salary FROM Employee 
        ORDER BY salary DESC LIMIT 1 OFFSET 1
    )
END as SecondHighestSalary;