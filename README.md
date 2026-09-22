# Fraud Detection & Transaction Monitoring Platform

A finance-risk portfolio project focused on transaction monitoring, rule-based detection, fraud features, model evaluation under severe class imbalance, and analyst-oriented alerts.

## Business problem

A digital payments company needs to detect suspicious transactions while controlling false positives.

## V1

1. Generate customers, accounts, devices, merchants, and transactions.
2. Load them into PostgreSQL.
3. Apply explainable SQL/Python rules.
4. Store alerts with reason codes.
5. Measure alert volume and fraud capture.

## V2

Train a classifier using transaction velocity, amount deviation, device novelty, merchant risk, and geographic signals. Evaluate with precision, recall, F1, and PR-AUC; do not rely on accuracy.

## Optional LangGraph extension

Build a fraud-investigation assistant that gathers evidence for an alert and summarizes it for a human analyst. It should not autonomously block accounts.
