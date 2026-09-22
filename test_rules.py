import pandas as pd
from src.rules import apply_rules


def test_high_amount_rule():
    df = pd.DataFrame([
        {"transaction_id": 1, "customer_id": 1, "amount": 20.0, "device_id": "dev-1", "country": "VN"},
        {"transaction_id": 2, "customer_id": 1, "amount": 6000.0, "device_id": "dev-1", "country": "VN"},
    ])
    alerts = apply_rules(df)
    assert ((alerts.transaction_id == 2) & (alerts.rule_code == "HIGH_AMOUNT")).any()
