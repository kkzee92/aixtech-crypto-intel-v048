# AIxTech crypto intel v0.48: paper-only trading information system

Research harness for automated cryptocurrency **information** and paper strategy evaluation. Does not place live orders, does not store exchange secrets, and is not financial advice.

Builds on [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo) secure AI-agent practices and prior kkzee92 versions.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.48.0-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Enhancements in v0.48

- Advanced multi-factor strategies: Supertrend proxy, Bollinger Band squeeze/expansion, volume profile / VWAP proxy, adaptive volatility clustering, multi-TF consistency, RSI divergence, MACD, ADX-like strength.
- Portfolio correlation risk gate and adaptive sizing under high vol/anomaly.
- Strengthened zero-trust: expanded redaction (BIP39, WIF, PEM, AWS, GitHub PATs, high-entropy), sealed multi-hash lineage, isolation anomaly detection, entropy scoring.
- Eight asset classes with refined playbooks and risk caps.
- Research only; synthetic fixtures recommended. AI-agent harness friendly (see AGENTS.md).

See [docs/asset-class-strategies.md](docs/asset-class-strategies.md) and [docs/security-architecture.md](docs/security-architecture.md).

## What it does

- Classifies into eight asset classes with enhanced multi-factor research rules.
- Labels regime (trend/range/stress) + volatility tier + anomaly score.
- Scores signal then multi-gate risk (class caps, confidence, correlation, anomaly).
- Paper fills with class costs; hash-chained audit with lineage seals.
- No live execution, no secret storage.

| Asset class | Enhanced research rule | Risk cap | Cost |
|---|---|---|---|
| Major | Supertrend + Bollinger + MACD + RSI div + multi-TF | 8% | 8 bps |
| Large-cap alt | Volume breakout + VWAP proxy + MACD + multi-TF | 4% | 14 bps |
| Stablecoin | Adaptive peg deviation (15-50 bps) | 0% | n/a |
| DeFi | Calm multi-scale + low anomaly + Supertrend | 2% | 22 bps |
| Meme | Qualified burst + StochRSI + consistency + hard horizon | 0.5% | 45 bps |
| L2 | Relative strength + MACD vs benchmark | 3% | 16 bps |
| RWA | Slow multi-scale + gap/anomaly halt | 2% | 12 bps |
| Perpetual | Negative funding carry + contained drift + low anomaly | 2% | 10 bps |

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m crypto_intel.demo
PYTHONPATH=src pytest tests/ -q
```

## Controls

Paper-only mode guard. No trade keys. Class caps, confidence floors, kill switch, drawdown, correlation, anomaly gates. Hash-chained audit + sealed lineage. Expanded redaction. PDPA-style tripwire. gitleaks recommended in CI.

## Honesty

No live connector included. Strategy scores describe synthetic data. Not financial, legal, or compliance advice. Research only.
