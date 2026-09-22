from __future__ import annotations
import pandas as pd


def apply_rules(df: pd.DataFrame) -> pd.DataFrame:
    alerts = []
    customer_avg = df.groupby("customer_id")["amount"].transform("mean").clip(lower=1)
    amount_ratio = df["amount"] / customer_avg

    for row, ratio in zip(df.itertuples(index=False), amount_ratio):
        if row.amount >= 5_000:
            alerts.append((row.transaction_id, "HIGH_AMOUNT", min(row.amount / 5_000, 10)))
        if ratio >= 12:
            alerts.append((row.transaction_id, "AMOUNT_DEVIATION", min(ratio / 12, 10)))
        if str(row.device_id).startswith("new-"):
            alerts.append((row.transaction_id, "NEW_DEVICE", 1.5))
        if row.country not in {"VN"}:
            alerts.append((row.transaction_id, "FOREIGN_COUNTRY", 1.2))

    return pd.DataFrame(alerts, columns=["transaction_id", "rule_code", "risk_score"])
