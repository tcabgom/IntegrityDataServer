import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)  # Listen for incoming connection

        print(f"Server listening on {self.host}:{self.port}")

        while True:
            _, addr = self.server_socket.accept()  # Accept incoming connection
            print(f"Connection established from {addr}")
            # Here, you can handle communication logic with the client
