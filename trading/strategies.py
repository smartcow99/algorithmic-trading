def simple_price_strategy(current_price, buy_price, sell_price):
    """
    간단한 가격 기반 매매 전략.
    - 매수: 현재 가격이 buy_price 이하일 때
    - 매도: 현재 가격이 sell_price 이상일 때
    """
    if current_price <= buy_price:
        return "BUY"
    elif current_price >= sell_price:
        return "SELL"
    return "HOLD"

def moving_average_strategy(short_ma, long_ma):
    """
    이동 평균 교차 전략.
    - 매수: 단기 이동 평균 > 장기 이동 평균
    - 매도: 단기 이동 평균 < 장기 이동 평균
    """
    if short_ma > long_ma:
        return "BUY"
    elif short_ma < long_ma:
        return "SELL"
    return "HOLD"
