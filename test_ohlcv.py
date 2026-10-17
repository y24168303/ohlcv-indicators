"""Quick sanity checks, no pytest needed:  python test_ohlcv.py"""
from ohlcv import sma, ema, rsi, atr


def main():
    assert sma([1, 2, 3, 4, 5], 3) == [None, None, 2.0, 3.0, 4.0]
    assert sma([], 2) == []
    assert sma([1.0], 5) == [None]
    assert ema([1, 1, 1, 1], 2) == [None, 1.0, 1.0, 1.0]
    r = rsi([4, 4.2, 4.3, 4.5, 4.9, 5.6, 5.8, 5.7, 6.0], 3)
    assert r[3] is not None and 50 < r[-1] <= 100, r
    a = atr([1, 1.2, 1.4], [0.9, 1.0, 1.2], [1.0, 1.1, 1.3], 2)
    assert a[1] is not None and a[2] is not None, a
    assert atr([1], [0.9], [1.0], 5) == [None]
    print("all checks passed")


if __name__ == "__main__":
    main()
