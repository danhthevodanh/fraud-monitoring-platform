from pathlib import Path
import pandas as pd
from src.rules import apply_rules

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "raw" / "transactions.csv")
alerts = apply_rules(df)
alerts.to_csv(ROOT / "data" / "raw" / "alerts.csv", index=False)

flagged = df.merge(alerts[["transaction_id"]].drop_duplicates(), on="transaction_id", how="inner")
precision = flagged["is_fraud"].mean() if len(flagged) else 0
recall = flagged["is_fraud"].sum() / max(df["is_fraud"].sum(), 1)
print(f"alerts: {len(alerts):,}")
print(f"transactions flagged: {flagged['transaction_id'].nunique():,}")
print(f"rule-level precision: {precision:.3%}")
print(f"fraud capture / recall: {recall:.3%}")
