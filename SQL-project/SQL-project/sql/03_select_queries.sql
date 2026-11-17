-- C. Query records
SELECT * FROM users;

SELECT * FROM calculations;

-- INNER JOIN
SELECT
    u.username,
    c.operation,
    c.operand_a,
    c.operand_b,
    c.result
FROM calculations c
JOIN users u
ON c.user_id = u.id;
