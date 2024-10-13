import socket
import sys


def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)


def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'terminate':
                print(f"Terminating server")
                break
            print(f"Received {message}")
    finally:
        client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
