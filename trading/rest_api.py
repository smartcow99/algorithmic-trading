import os
import time
import uuid

import jwt
import requests
from dotenv import load_dotenv

# .env 파일에서 API 키와 Secret 키 로드
load_dotenv()

ACCESS_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_URL = "https://api.bithumb.com"

def get_authorization_token():
    """
    빗썸 API에 필요한 JWT 인증 토큰 생성
    """
    payload = {
        'access_key': ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000)
    }
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return f'Bearer {jwt_token}'

def get_accounts():
    """
    빗썸 전체 계좌 조회
    """
    url = f"{BASE_URL}/v1/accounts"
    headers = {
        'Authorization': get_authorization_token()
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API Error: {response.status_code}")
            print(response.json())
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_current_price(ticker):
    """
    빗썸 현재 시세 조회
    """
    url = f"{BASE_URL}/public/ticker/{ticker}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == '0000':
                return float(data['data']['closing_price'])  # 현재가 반환
        return 0.0  # 실패 시 0 반환
    except Exception as e:
        print(f"An error occurred while fetching price for {ticker}: {e}")
        return 0.0

def print_accounts_with_profit():
    """
    계좌 정보를 조회하고 평가 금액, 수익 금액, 수익률 계산 및 출력
    """
    accounts = get_accounts()
    if accounts and isinstance(accounts, list):  # accounts가 리스트인지 확인
        print("\n계좌 수익 정보:")
        for account in accounts:
            currency = account.get("currency", "N/A")
            balance = float(account.get("balance", "0"))
            avg_buy_price = float(account.get("avg_buy_price", "0"))

            # KRW는 제외 (평가 금액 계산 불필요)
            if currency == "KRW" or balance == 0:
                continue

            # 현재 화폐의 시세 가져오기
            ticker = f"{currency}_KRW"
            current_price = get_current_price(ticker)

            # 총 평가 금액 및 수익 계산
            evaluation = balance * current_price  # 평가 금액
            profit = evaluation - (balance * avg_buy_price)  # 수익 금액
            profit_rate = (profit / (balance * avg_buy_price)) * 100 if avg_buy_price > 0 else 0  # 수익률

            # 출력
            print(f"- 화폐: {currency}")
            print(f"  잔고: {balance:.4f}")
            print(f"  현재 시세: {int(current_price)} KRW")  # KRW는 정수로 출력
            print(f"  평가 금액: {int(evaluation)} KRW")  # 평가 금액 정수
            print(f"  매수 평균가: {int(avg_buy_price)} KRW")  # 매수 평균가 정수
            print(f"  수익 금액: {int(profit)} KRW")  # 수익 금액 정수
            print(f"  수익률: {profit_rate:.2f} %")
            print("-" * 30)
    else:
        print("계좌 정보를 가져올 수 없거나 데이터 형식이 올바르지 않습니다.")

if __name__ == "__main__":
    print_accounts_with_profit()
