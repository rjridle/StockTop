import requests

api_key = 'c29hu7qad3ie4ecb6r50'
webhook_secret = 'c29hu7qad3ie4ecb6r60'
sandbox_api_key = 'sandbox_c29hu7qad3ie4ecb6r5g'

import websocket

def on_message(ws, message):
    print('PRINTING on_message')
    print(message)

def on_error(ws, error):
    print('PRINTING on_error')
    print(error)

def on_close(ws):
    print('PRINTING on_close')
    print("### closed ###")

def on_open(ws):
    print('SENDING on_open')
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    token_address = "wss://ws.finnhub.io?token=c29hu7qad3ie4ecb6r50"
    ws = websocket.WebSocketApp(token_address,on_message = on_message,on_error = on_error,on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

# Register new webhook for earnings
#add_request = 'https://finnhub.io/api/v1/webhook/add?token=c29hu7qad3ie4ecb6r50'
#r = requests.post(add_request, json={'event': 'earnings', 'symbol': 'AAPL'})
#res = r.json()
#print(res)

#webhook_id = res['id']
# List webhook
#get_request = 'https://finnhub.io/api/v1/webhook/list?token=c29hu7qad3ie4ecb6r50'
#r = requests.get(get_request)
#res = r.json()
#print(res)

#Delete webhook
#post_request = 'https://finnhub.io/api/v1/webhook/delete?token='
#r = requests.post(post_request, json={'id': webhook_id})
#res = r.json()
#print(res)
