# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person LEFT OUTER JOIN Address
ON Person.personId = Address.personId;