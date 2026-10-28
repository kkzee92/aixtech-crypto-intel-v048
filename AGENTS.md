# Agent rules for this repository

This is a paper-only research system. Follow these rules when using AI coding agents.

1. Never include real API keys, private keys, seed phrases, wallet addresses, or personal data in code, tests, fixtures, or prompts.
2. All market data must be synthetic or clearly labeled public/open data. Use fixtures.
3. Do not implement live order placement or withdrawal logic. Paper mode only.
4. Prefer transparent, testable heuristics over black-box models.
5. Run tests and lint locally before proposing changes.
6. Document any AI assistance in commit messages or PRs.
7. Keep security controls (redaction, audit lineage) intact or strengthen them.
8. Asset-class risk caps and confidence floors are hard constraints.

Human review required for any strategy or risk-gate changes.
