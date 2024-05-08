# Write your MySQL query statement below
SELECT x,y,z,
CASE
    WHEN x < 0 OR y < 0 OR z < 0 THEN 'No'
    WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
    ELSE 'No'
END AS triangle
FROM Triangle;
