# Write your MySQL query statement below
-- SELECT MAX(salary) AS secondHighestSalary
-- FROM employee
-- WHERE salary < (
--     SELECT MAX(salary)
--     FROM employee
-- )

SELECT
    IFNULL(
        (
            SELECT DISTINCT salary
            FROM employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET 1
        ),
    NULL
) AS secondHighestSalary;