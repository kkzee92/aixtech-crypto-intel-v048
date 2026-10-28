"""Simple demo runner."""
from crypto_intel.models import AssetClass, Candle, ExecutionMode
from crypto_intel.strategies import signal_for
from crypto_intel.security import assert_paper_only, AuditLog
from crypto_intel.risk import apply_risk_gates

def run_demo() -> None:
    assert_paper_only(ExecutionMode.PAPER)
    # Synthetic candles
    candles = [
        Candle("BTCUSDT", AssetClass.MAJOR, 60000, 61000, 59500, 60500, 1000),
        Candle("BTCUSDT", AssetClass.MAJOR, 60500, 62000, 60000, 61500, 1200),
        Candle("BTCUSDT", AssetClass.MAJOR, 61500, 63000, 61000, 62500, 1100),
        Candle("BTCUSDT", AssetClass.MAJOR, 62500, 64000, 62000, 63500, 1300),
        Candle("BTCUSDT", AssetClass.MAJOR, 63500, 65000, 63000, 64500, 1400),
        Candle("BTCUSDT", AssetClass.MAJOR, 64500, 66000, 64000, 65500, 1500),
        Candle("BTCUSDT", AssetClass.MAJOR, 65500, 67000, 65000, 66500, 1600),
        Candle("BTCUSDT", AssetClass.MAJOR, 66500, 68000, 66000, 67500, 1700),
    ]
    sig = signal_for(candles)
    gated = apply_risk_gates(sig, anomaly_score=0.5)
    log = AuditLog()
    log.append("signal_generated", gated.reason)
    print(f"Signal: {gated.side.value} {gated.symbol} conf={gated.confidence:.2f} size={gated.size_pct:.3f} reason={gated.reason}")
    print(f"Audit verified: {log.verify()}")

if __name__ == "__main__":
    run_demo()
