# Cyber and data security architecture (v0.48)

Zero-trust design for paper-only research system.

## Principles
- No secret storage. Redaction on all logs and outputs.
- Paper-only execution mode enforced.
- Append-only hash-chained audit log with sealed lineage (timestamp + source hash).
- Entropy-based high-entropy string detection.
- Expanded secret patterns: API keys, WIF, PEM private keys, AWS access keys, GitHub PATs, BIP39 seed proxies, wallet addresses.
- Isolation anomaly scoring (feature z-scores) to reduce size on outliers.
- Data classification: public market data vs secrets (never retained).

## Controls
- `assert_paper_only` guard.
- `redact` and `contains_secret` tripwires.
- `AuditLog` with `verify()` for integrity.
- Recommended: gitleaks in CI, synthetic fixtures only, human review for strategy changes.

Inspired by secure AI-agent harness practices from zeekiankok92.

Not production security. Research demonstration only.
