# ohlcv-indicators

Tiny OHLCV technical-indicator toolkit for Python. **Standard library only, zero dependencies.**

## Usage

```python
from ohlcv import sma, ema, rsi, atr

closes = [10.0, 10.4, 10.2, 10.9, 11.1, 10.8, 11.2, 11.5, 11.3, 11.8]

sma(closes, 5)     # simple moving average
ema(closes, 12)    # exponential moving average (SMA-seeded)
rsi(closes, 14)    # relative strength index
atr(highs, lows, closes, 14)  # average true range (Wilder smoothing)
```

Series are returned as lists aligned with the input; positions where the
window is not yet full are `None`.

## Run the sanity checks

```bash
python test_ohlcv.py
```

MIT.
