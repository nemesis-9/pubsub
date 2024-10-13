import socket
import sys
import threading
from pubsub import pub

clients = {}
topics = {}


def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()


def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message.startswith("subscribe:"):
                topic = message.split(":")[1]
                if topic not in topics:
                    topics[topic] = []
                topics[topic].append(client_socket)
                print(f"Client subscribed to topic {topic}")
            elif message.lower() == 'terminate':
                print(f"Terminating server")
                break
            else:
                topic, message = message.split(":", 1)
                if topic in topics:
                    for client in topics[topic]:
                        try:
                            client.sendall(message.encode())
                        except:
                            topics[topic].remove(client)
    finally:
        client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
