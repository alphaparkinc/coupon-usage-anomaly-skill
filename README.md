# coupon-usage-anomaly-skill

> **GenPark AI Agent Skill** -- Coupon abuse fraud detection auditor.

## Quick Start

```python
from client import CouponUsageAnomalyClient
client = CouponUsageAnomalyClient()
res = client.audit_redemption("WELCOME10", 25, 10.0)
print(res["anomaly_detected"])
```
