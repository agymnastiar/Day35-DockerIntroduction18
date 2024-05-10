CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,
    gender VARCHAR(10),
    age INTEGER,
    annual_income NUMERIC,
    spending_score INTEGER,
    profession VARCHAR(50),
    work_experience NUMERIC,
    family_size INTEGER
);

\copy Customers(gender, age, annual_income, spending_score, profession, work_experience, family_size) FROM '/data/Customers.csv' DELIMITER ',' CSV HEADER;