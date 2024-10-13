import socket
import sys


def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to {server_ip}:{server_port}")

    try:
        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode())
            if message.lower() == 'terminate':
                print("Terminating client")
                break

    finally:
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
