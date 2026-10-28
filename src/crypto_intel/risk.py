"""Risk gates and adaptive sizing (v0.48)."""
from __future__ import annotations
from crypto_intel.models import Signal

CLASS_CAPS = {
    "major": 0.08,
    "large_alt": 0.04,
    "stable": 0.0,
    "defi": 0.02,
    "meme": 0.005,
    "l2": 0.03,
    "rwa": 0.02,
    "perp": 0.02,
}

def apply_risk_gates(signal: Signal, anomaly_score: float = 0.0, correlation: float = 0.0) -> Signal:
    cap = CLASS_CAPS.get(signal.asset_class.value, 0.01)
    size = min(signal.size_pct, cap)
    if anomaly_score > 2.5 or correlation > 0.75:
        size *= 0.5
    if signal.confidence < 0.55:
        size = 0.0
    return Signal(signal.symbol, signal.asset_class, signal.side, signal.confidence, signal.reason, signal.stop_pct, size, signal.horizon)
