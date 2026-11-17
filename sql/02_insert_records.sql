-- B. Insert records
INSERT INTO users (username, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob',   'bob@example.com');

INSERT INTO calculations (user_id, operation, operand_a, operand_b, result) VALUES
    (1, 'add',      2,  3,  5),
    (1, 'divide',   10, 2,  5),
    (2, 'multiply', 4,  5,  20);
