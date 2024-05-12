from flask import Flask, render_template
from websocket_server import WebsocketServer
import threading
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def run():
    app.run(debug=False, host='0.0.0.0', port=5000)
    

# Called for every client connecting (after handshake)
def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])

# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])

# Called when a client sends a message
def message_received(client, server, message):
    print("Client(%d) said: %s" % (client['id'], message))
    server.send_message_to_all("Client(%d) said: %s" % (client['id'], message))

def forever():
    while True:
        server.send_message_to_all("Hello from the server!")
        time.sleep(1)

        
if __name__ == '__main__':
    # Start the WebSocket server
    server = WebsocketServer(port=6603, host='0.0.0.0')

    # Assigning the functions to the events
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)

    # Start the WebSocket server in a separate thread
    ws_thread = threading.Thread(target=server.run_forever)
    ws_thread.start()

    runThread = threading.Thread(target=run)
    runThread.start()

    foreverThread = threading.Thread(target=forever)
    foreverThread.start()

    print("WebSocket server started on port 6603")

    

    # Start the Flask application
    ws_thread.join()
    runThread.join()
    foreverThread.join()
