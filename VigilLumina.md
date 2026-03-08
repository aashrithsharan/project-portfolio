# 🛡️ Vigil Lumina

> **Real-time Fraud Decisioning Platform MVP**  
> _Detects payment fraud in <300ms using Hybrid AI (XGBoost + Heuristics) and Explainable Risk Scoring._

---

## 🎬 30-Second Demo

**1. Start the Platform**
```bash
docker-compose up --build
```

**2. Run the Live Demo Script**
(In a new terminal)
```bash
python scripts/demo.py
```
*   Generates 50 realistic transactions.
*   Simulates fraud attacks (velocity spikes, high-value anomalies).
*   Opens the Analyst Dashboard in your browser.

**3. Explore the UI**
*   **Home:** See live latency and fraud rate stats.
*   **Analyst Dashboard:** Review flagged transactions and mark false positives.
*   **Config:** Adjust risk thresholds in real-time.

---

## 🏗️ Architecture

```ascii
[ User / Payment Gateway ]
        | (JSON)
        v
+----------------+      +------------------+
|   API Gateway  | ---> |  SQLite (Stats)  |
| (FastAPI 8000) |      +------------------+
+----------------+
        |
        v
+----------------+      +------------------+
| Decision Engine| <--- |   Models (AI)    |
| (Rules + XGB)  |      | (XGBoost .bin)   |
+----------------+      +------------------+
        |
        v
   [ Response ]
  { "decision": "DECLINE", "score": 0.98 }
```

---

## 💰 Business Use Cases

1.  **E-commerce Checkout:** Block stolen credit cards instantly before shipping goods.
2.  **Account Takeover (ATO):** Detect new devices accessing accounts from high-risk countries.
3.  **Promo Abuse:** Prevent users from creating 100 accounts to claim signup bonuses.

---

## 🔗 API Documentation

Once running, access Swagger UI at: `[URL_REMOVED]

### POST `/score`
Scoring endpoint for transactions.

**Request:**
```json
{
  "transaction_id": "tx_123",
  "user_id": "user_john",
  "device_id": "iphone_12",
  "amount": 250.50,
  "country": "US",
  "merchant": "Amazon",
  "timestamp": "2024-03-20T10:00:00"
}
```

**Response:**
```json
{
  "transaction_id": "tx_123",
  "score": 0.85,
  "decision": "DECLINE",
  "reasons": ["High Velocity", "New Country"]
}
```

### GET `/metrics`
Returns system health KPIs.

```json
{
  "total_requests": 1542,
  "fraud_rate": 2.4,
  "avg_latency": 145.2,
  "review_queue": 15
}
```