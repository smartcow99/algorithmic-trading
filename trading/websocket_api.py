import json

import websocket


def on_message(ws, message):
    """
    서버로부터 메시지를 받을 때 호출되는 함수
    """
    data = json.loads(message)
    print(json.dumps(data, indent=2))  # 수신 데이터 출력

def on_error(ws, error):
    """
    WebSocket 에러 발생 시 호출되는 함수
    """
    print(f"WebSocket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    """
    WebSocket 연결이 종료될 때 호출되는 함수
    """
    print("WebSocket connection closed")

def on_open(ws):
    """
    WebSocket 연결이 열릴 때 호출되는 함수
    """
    print("WebSocket connection opened")

    # 구독 메시지 전송
    subscribe_message = {
        "type": "ticker",
        "symbols": ["BTC_KRW"],  # 구독할 심볼
        "tickTypes": ["1M"]     # 데이터 타입
    }
    ws.send(json.dumps(subscribe_message))

def subscribe_ticker():
    """
    WebSocket 연결을 생성하고 실시간 데이터를 수신
    """
    url = "wss://pubwss.bithumb.com/pub/ws"
    ws = websocket.WebSocketApp(
        url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    subscribe_ticker()
