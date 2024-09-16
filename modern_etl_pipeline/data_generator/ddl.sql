drop table customers cascade;
drop table accounts cascade;
drop table events cascade;
drop table transactions cascade;

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    occupation VARCHAR(100)
);

CREATE TABLE accounts (
    account_number VARCHAR(20) PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    account_type VARCHAR(50),
    balance DECIMAL(10, 2),
    opened_at DATE,
    branch_name VARCHAR(50),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,  -- Surrogate key for each transaction
    account_number VARCHAR(20) REFERENCES accounts(account_number),
    transaction_date TIMESTAMP,  -- This field no longer needs to be part of the primary key
    merchant VARCHAR(100),
    amount DECIMAL(10, 2),
    transaction_type VARCHAR(50),
    transaction_location VARCHAR(50),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE events (
    event_id VARCHAR(50) PRIMARY KEY,  -- Surrogate key for each event
    customer_id INT REFERENCES customers(customer_id),
    event_date TIMESTAMP,
    event_type VARCHAR(50),
    device VARCHAR(50),
    ip_address VARCHAR(20),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);