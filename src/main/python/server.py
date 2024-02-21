import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # Aumentado el número de conexiones en cola

        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()  # Accept incoming connection
            print(f"Connection established from {addr}")

            # Manejar la comunicación con el cliente en un hilo separado
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)  # Recibir datos del cliente
                if not data:
                    break  # Si no hay datos, el cliente ha cerrado la conexión

                received_message = data.decode()
                print(f"Received message from {client_socket.getpeername()}: {received_message}")

                # Responder al cliente
                response_message = "Server received your message: " + received_message
                client_socket.sendall(response_message.encode())
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

# Ejemplo

