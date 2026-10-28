"""Core data models."""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class AssetClass(Enum):
    MAJOR = "major"
    LARGE_ALT = "large_alt"
    STABLE = "stable"
    DEFI = "defi"
    MEME = "meme"
    L2 = "l2"
    RWA = "rwa"
    PERP = "perp"

class Side(Enum):
    LONG = "long"
    SHORT = "short"
    FLAT = "flat"

class ExecutionMode(Enum):
    PAPER = "paper"

@dataclass
class Candle:
    symbol: str
    asset_class: AssetClass
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestamp: str = ""

@dataclass
class Signal:
    symbol: str
    asset_class: AssetClass
    side: Side
    confidence: float
    reason: str
    stop_pct: float
    size_pct: float
    horizon: int

@dataclass
class AuditEvent:
    sequence: int
    action: str
    detail: str
    previous_hash: str
    digest: str
    seal: str = ""
