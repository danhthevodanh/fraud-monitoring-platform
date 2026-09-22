CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS fraud;

CREATE TABLE IF NOT EXISTS raw.transactions (
    transaction_id BIGINT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    transaction_time TIMESTAMP NOT NULL,
    amount NUMERIC(15,2) NOT NULL CHECK (amount >= 0),
    merchant_id BIGINT NOT NULL,
    country VARCHAR(2) NOT NULL,
    device_id VARCHAR(64) NOT NULL,
    is_fraud BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS fraud.alerts (
    alert_id BIGSERIAL PRIMARY KEY,
    transaction_id BIGINT NOT NULL,
    rule_code VARCHAR(64) NOT NULL,
    risk_score NUMERIC(8,4),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
