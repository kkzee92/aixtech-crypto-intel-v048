from crypto_intel.models import AssetClass, Candle
from crypto_intel.strategies import signal_for
from crypto_intel.security import AuditLog, redact

def test_signal_and_audit():
    candles = [Candle("TEST", AssetClass.MAJOR, 100, 105, 98, 102 + i, 1000) for i in range(10)]
    sig = signal_for(candles)
    assert sig.side.value in ("long", "flat")
    log = AuditLog()
    log.append("test", "no secrets here")
    assert log.verify()
    assert "[REDACTED]" in redact("api_key=sk_live_abcdef123456")
