"""
server.py
Simple TCP server for CYB333 midterm.
Listens for a client, receives messages, and sends responses back.
"""

import socket

HOST = "127.0.0.1"  # localhost
PORT = 5001         # changed from 5000 because it was already in use


def start_server():
    """Start a simple TCP server that accepts a single client connection."""
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow quick reuse of the port if we restart the server
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind the socket to an address and port
        print("[DEBUG] Binding server socket...")
        server_socket.bind((HOST, PORT))
        print(f"[SERVER] Listening on {HOST}:{PORT} ...")

        # Listen for incoming connections (backlog of 1 is fine for this demo)
        server_socket.listen(1)

        # Wait for a client to connect
        print("[SERVER] Waiting for a client to connect...")
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connected by {addr}")

        # Use a context manager to ensure the client socket closes cleanly
        with conn:
            while True:
                # Receive data from client (up to 1024 bytes)
                data = conn.recv(1024)

                # If no data is received, client disconnected
                if not data:
                    print("[SERVER] Client disconnected.")
                    break

                # Decode bytes to string
                message = data.decode("utf-8")
                print(f"[SERVER] Received from client: {message}")

                # Build a response and send back
                response = f"Server received: {message}"
                conn.sendall(response.encode("utf-8"))

    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down (KeyboardInterrupt).")
    except Exception as e:
        print(f"[SERVER] Error: {e}")
    finally:
        # Always close the server socket
        server_socket.close()
        print("[SERVER] Server socket closed.")


if __name__ == "__main__":
    print("[DEBUG] in __main__ guard")
    start_server()
