from src.main.python.client import Client
from src.main.python.server import Server

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Change this to the server's IP address
    PORT = 12345  # Server listening port

    server = Server(HOST, PORT)
    client = Client(HOST, PORT)

    # Start the server in a separate thread
    import threading
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # Connect the client to the server
    client.connect()