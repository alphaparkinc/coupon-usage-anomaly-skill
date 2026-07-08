"""
example_usage.py -- Demonstrates CouponUsageAnomalyClient
"""
from client import CouponUsageAnomalyClient

def main():
    client = CouponUsageAnomalyClient()
    result = client.audit_redemption(
        coupon_code="WINTER20",
        daily_redeemed_count=450,
        average_daily_redemptions=50.0
    )
    print("[Coupon Anomaly Check]")
    print(f"Anomaly Detected: {result['anomaly_detected']}")
    print(f"Risk Tier: {result['risk_level'].upper()} (Ratio: {result['velocity_ratio']}x)")

if __name__ == "__main__":
    main()
