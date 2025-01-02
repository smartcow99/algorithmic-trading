from trading.strategies import simple_price_strategy, moving_average_strategy

def test_simple_price_strategy():
    assert simple_price_strategy(48000000, 47000000, 49000000) == "HOLD"
    assert simple_price_strategy(46000000, 47000000, 49000000) == "BUY"
    assert simple_price_strategy(50000000, 47000000, 49000000) == "SELL"

def test_moving_average_strategy():
    assert moving_average_strategy(47500000, 47800000) == "SELL"
    assert moving_average_strategy(48000000, 47800000) == "BUY"
