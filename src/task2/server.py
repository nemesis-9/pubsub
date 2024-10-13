import socket
import sys
import threading
from pubsub import pub

clients = []


def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Accepted connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()


def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'terminate':
                print(f"Terminating server")
                break
            pub.sendMessage("message", message=message)
    finally:
        client_socket.close()
        clients.remove(client_socket)


def handle_message(message):
    for client in clients:
        try:
            client.sendall(message.encode())
        except:
            clients.remove(client)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    pub.subscribe(handle_message, "message")
    start_server(port)