import socket
import sys


def start_client(server_ip, server_port, role):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to {server_ip}:{server_port} as {role}")

    if role.lower() == "publisher":
        publisher_mode(client_socket)
    elif role.lower() == "subscriber":
        subscriber_mode(client_socket)
    else:
        print("Invalid role. Use publisher or subscriber.")
        client_socket.close()


def publisher_mode(client_socket):
    try:
        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode())
            if message.lower() == 'terminate':
                print("Terminating client")
                break

    finally:
        client_socket.close()


def subscriber_mode(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message: {message}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python client.py <server_ip> <server_port> <role>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    role = sys.argv[3]
    start_client(server_ip, server_port, role)
