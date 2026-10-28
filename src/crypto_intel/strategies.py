"""Enhanced multi-factor strategies per asset class (v0.48)."""
from __future__ import annotations
from statistics import fmean, pstdev
from crypto_intel.models import AssetClass, Candle, Side, Signal

def _ema(values: list[float], span: int) -> float:
    if not values:
        return 0.0
    alpha = 2.0 / (span + 1)
    value = values[0]
    for point in values[1:]:
        value = alpha * point + (1 - alpha) * value
    return value

def _macd_proxy(closes: list[float]) -> float:
    if len(closes) < 26:
        return 0.0
    return _ema(closes, 12) - _ema(closes, 26)

def _rsi(closes: list[float], period: int = 14) -> float:
    if len(closes) < period + 1:
        return 50.0
    changes = [closes[i] / closes[i - 1] - 1.0 for i in range(1, len(closes))]
    gains = [max(c, 0.0) for c in changes[-period:]]
    losses = [abs(min(c, 0.0)) for c in changes[-period:]]
    avg_loss = fmean(losses) if losses else 0.0
    if avg_loss == 0:
        return 100.0
    rs = fmean(gains) / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))

def _bollinger(closes: list[float], period: int = 20) -> tuple[float, float, float]:
    if len(closes) < period:
        return closes[-1], closes[-1], closes[-1]
    window = closes[-period:]
    mid = fmean(window)
    std = pstdev(window) or 0.01
    return mid - 2 * std, mid, mid + 2 * std

def _supertrend_proxy(candles: list[Candle], period: int = 10) -> bool:
    if len(candles) < period:
        return False
    # Simplified: close above average of highs/lows adjusted for ATR-like
    recent = candles[-period:]
    avg_hl = fmean([(c.high + c.low) / 2 for c in recent])
    return candles[-1].close > avg_hl

def signal_for(candles: list[Candle], benchmark: list[Candle] | None = None) -> Signal:
    if len(candles) < 8:
        raise ValueError("need at least 8 candles")
    ac = candles[-1].asset_class
    closes = [c.close for c in candles]
    macd = _macd_proxy(closes)
    rsi = _rsi(closes)
    lower, mid, upper = _bollinger(closes)
    super_ok = _supertrend_proxy(candles)
    vol = pstdev(closes[-10:]) / fmean(closes[-10:]) if len(closes) >= 10 else 0.05

    if ac is AssetClass.MAJOR and super_ok and macd > 0 and 35 <= rsi <= 75 and candles[-1].close > mid:
        return Signal(candles[-1].symbol, ac, Side.LONG, 0.75, "major: Supertrend+Bollinger+MACD+RSI", 0.02, 0.07, 16)
    if ac is AssetClass.LARGE_ALT and macd > 0 and candles[-1].volume > fmean([c.volume for c in candles[-5:]]) * 1.15 and super_ok:
        return Signal(candles[-1].symbol, ac, Side.LONG, 0.68, "large-alt: volume breakout + Supertrend + MACD", 0.03, 0.035, 10)
    if ac is AssetClass.STABLE:
        return Signal(candles[-1].symbol, ac, Side.FLAT, 0.9, "stable: peg monitor only", 0.0, 0.0, 1)
    if ac is AssetClass.DEFI and super_ok and vol < 0.06 and macd > 0:
        return Signal(candles[-1].symbol, ac, Side.LONG, 0.62, "defi: calm Supertrend + low vol", 0.04, 0.018, 12)
    if ac is AssetClass.MEME and (candles[-1].close / candles[-4].close - 1) > 0.12 and rsi < 80:
        return Signal(candles[-1].symbol, ac, Side.LONG, 0.55, "meme: qualified burst", 0.08, 0.004, 3)
    # Similar stubs for L2, RWA, PERP
    if ac is AssetClass.L2 and macd > 0 and super_ok:
        return Signal(candles[-1].symbol, ac, Side.LONG, 0.65, "l2: relative strength proxy", 0.025, 0.025, 10)
    if ac is AssetClass.RWA and super_ok and vol < 0.04:
        return Signal(candles[-1].symbol, ac, Side.LONG, 0.60, "rwa: slow multi-scale", 0.015, 0.015, 20)
    if ac is AssetClass.PERP and macd < 0 and vol < 0.05:
        return Signal(candles[-1].symbol, ac, Side.SHORT, 0.58, "perp: contained negative momentum", 0.02, 0.015, 8)
    return Signal(candles[-1].symbol, ac, Side.FLAT, 0.4, "no enhanced edge", 0.01, 0.0, 1)
