from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(42)
N = 150_000

customer_id = rng.integers(1, 8_001, N)
base_amount = rng.lognormal(3.5, 0.9, N)
is_fraud = rng.random(N) < 0.004
amount = base_amount * np.where(is_fraud, rng.uniform(5, 25, N), 1.0)
new_country = np.where(is_fraud & (rng.random(N) < 0.5), "DE", "VN")
new_device = np.where(is_fraud & (rng.random(N) < 0.6), [f"new-{i}" for i in range(N)], [f"dev-{c%5000}" for c in customer_id])

start = pd.Timestamp("2026-01-01")
transaction_time = start + pd.to_timedelta(rng.integers(0, 240*24*60, N), unit="m")

df = pd.DataFrame({
    "transaction_id": np.arange(1, N+1),
    "customer_id": customer_id,
    "transaction_time": transaction_time,
    "amount": np.round(amount, 2),
    "merchant_id": rng.integers(1, 2_001, N),
    "country": new_country,
    "device_id": new_device,
    "is_fraud": is_fraud,
}).sort_values("transaction_time")

df.to_csv(OUT / "transactions.csv", index=False)
print(df["is_fraud"].value_counts())
print(OUT / "transactions.csv")
