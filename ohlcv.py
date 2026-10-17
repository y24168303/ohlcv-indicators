"""Tiny OHLCV indicator toolkit. Pure standard library, no dependencies.

Series are returned as lists aligned with the input; positions where the
window is not yet full are None.
"""


def sma(values, period):
    """Simple moving average over values with the given period."""
    if period < 1:
        raise ValueError("period must be >= 1")
    out = [None] * len(values)
    for i in range(period - 1, len(values)):
        out[i] = sum(values[i - period + 1: i + 1]) / period
    return out


def ema(values, period):
    """Exponential moving average, seeded with the SMA of the first
    period values."""
    if period < 1:
        raise ValueError("period must be >= 1")
    out = [None] * len(values)
    if len(values) < period:
        return out
    k = 2.0 / (period + 1)
    prev = sum(values[:period]) / period
    out[period - 1] = prev
    for i in range(period, len(values)):
        prev = values[i] * k + prev * (1.0 - k)
        out[i] = prev
    return out


def rsi(closes, period=14):
    """Relative Strength Index (Cutler's SMA variant)."""
    n = len(closes)
    if n <= period:
        return [None] * n
    gains, losses = [], []
    for i in range(1, n):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    out = [None] * n
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    out[period] = 100.0 if avg_loss == 0 else 100.0 - 100.0 / (1 + avg_gain / avg_loss)
    for i in range(period + 1, n):
        avg_gain = (avg_gain * (period - 1) + gains[i - 1]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i - 1]) / period
        out[i] = 100.0 if avg_loss == 0 else 100.0 - 100.0 / (1 + avg_gain / avg_loss)
    return out


def atr(highs, lows, closes, period=14):
    """Average True Range with Wilder smoothing."""
    if len(closes) != len(highs) or len(closes) != len(lows):
        raise ValueError("highs/lows/closes must have equal length")
    if period < 1:
        raise ValueError("period must be >= 1")
    n = len(closes)
    out = [None] * n
    if n < period:
        return out
    trs = [highs[0] - lows[0]]
    for i in range(1, n):
        trs.append(max(highs[i] - lows[i],
                       abs(highs[i] - closes[i - 1]),
                       abs(lows[i] - closes[i - 1])))
    prev = sum(trs[:period]) / period
    out[period - 1] = prev
    for i in range(period, n):
        prev = (prev * (period - 1) + trs[i]) / period
        out[i] = prev
    return out
