# Asset-class strategy notes (v0.48)

Research heuristics with advanced multi-factor enhancements (Supertrend proxy, Bollinger, volume/VWAP, adaptive vol, multi-TF, RSI div, MACD, ADX-like).

Regime classification: trend / range / stress based on realized moves and ranges.

## Major
Hypothesis: liquid majors trend with confirmation. Entry: Supertrend proxy + close > Bollinger mid + MACD >0 + RSI 35-75 + multi-TF align. Cap 8%. Horizon ~16. Cost 8 bps.

## Large-cap alt
Hypothesis: volume-confirmed breakouts. Entry: volume >1.15x recent + Supertrend + MACD. Cap 4%.

## Stablecoin
Peg integrity only. Adaptive bands. Size zero.

## DeFi
Calm regimes only. Supertrend + vol <6% + MACD. Cap 2%.

## Meme
Rare bursts (e.g. >12% in 4 bars) with RSI not extreme. Horizon 3. Cap 0.5%.

## L2
Relative strength proxies + Supertrend/MACD. Cap 3%.

## RWA
Slow multi-scale, low vol, gap controls. Cap 2%.

## Perpetual
Contained momentum / funding proxies. Cap 2%.

All subject to anomaly, correlation, and confidence gates. Research only.
