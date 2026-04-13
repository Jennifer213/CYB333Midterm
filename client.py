"""
client.py
Simple TCP client for CYB333 midterm.
Connects to the server, sends user input, and prints server responses.
"""

import socket

HOST = "127.0.0.1"  # must match the server
PORT = 5001         # must match the server's port


def run_client():
    """Connect to the server and send messages until user types 'quit'."""
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"[CLIENT] Connecting to {HOST}:{PORT} ...")
        client_socket.connect((HOST, PORT))
        print("[CLIENT] Connected to server.\n")

        # Keep sending messages until the user quits
        while True:
            message = input("Enter message (or 'quit' to exit): ")

            if message.lower() == "quit":
                print("[CLIENT] Closing connection...")
                break

            # Send the message to the server
            client_socket.sendall(message.encode("utf-8"))

            # Receive and print the server's response
            data = client_socket.recv(1024)
            print(f"[CLIENT] Received from server: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("[CLIENT] Connection refused. Is the server running?")
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        # Always close the connection
        client_socket.close()
        print("[CLIENT] Client shutdown complete.")
