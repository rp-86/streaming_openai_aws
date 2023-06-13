import websocket
import ssl
import json

def on_message(ws, message):
    print("Received message:", message)

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, a, b):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection opened")
    # Send a request after the connection is opened
    request = {
        "action": "openai",
        "query":"What is AI?"
    }
    ws.send(json.dumps(request))

if __name__ == "__main__":
    # Specify your WebSocket API Gateway endpoint URL
    websocket_url = "wss://er7uagkgg4.execute-api.ap-south-1.amazonaws.com/dev"

    # Create a WebSocket connection
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Use SSL/TLS for secure WebSocket connection
    ws.on_open = on_open
    ws.run_forever()
