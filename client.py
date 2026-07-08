"""
coupon-usage-anomaly-skill: Client SDK
Flags checkout coupon code usage velocities when they spike above baseline standard limits.
"""
from __future__ import annotations
from typing import Optional


class CouponUsageAnomalyClient:
    """
    SDK for promotional abuse monitoring.
    """

    def audit_redemption(
        self,
        coupon_code: str,
        daily_redeemed_count: int,
        average_daily_redemptions: float,
    ) -> dict:
        base = max(1.0, average_daily_redemptions)
        ratio = daily_redeemed_count / base

        anomaly = ratio > 3.0  # Spikes of more than 3x the normal rate
        
        if ratio > 5.0:
            risk = "high"
        elif ratio > 2.0:
            risk = "medium"
        else:
            risk = "low"

        return {
            "coupon_code": coupon_code,
            "anomaly_detected": anomaly,
            "risk_level": risk,
            "velocity_ratio": round(ratio, 2)
        }
