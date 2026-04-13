"""
port_scanner.py
Simple TCP port scanner for CYB333 midterm.

Ethical use only:
- Allowed: localhost (127.0.0.1) and scanme.nmap.org
- Do NOT scan other hosts without permission.
"""

import socket
import time
from datetime import datetime


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Try to connect to the given host and port.
    Returns True if the port is open, False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        return result == 0  # 0 = open


def main():
    print("=== Simple Python Port Scanner (CYB333 Midterm) ===")
    print("Only scan 127.0.0.1 and scanme.nmap.org.\n")

    host = input("Enter target host (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("[ERROR] Invalid port range. Ports must be 1–65535, and start <= end.")
            return

    except ValueError:
        print("[ERROR] Ports must be integers.")
        return

    print(f"\n[INFO] Starting scan of {host} ({start_port}–{end_port})")
    print(f"[INFO] Scan started at: {datetime.now()}\n")

    try:
        for port in range(start_port, end_port + 1):
            is_open = scan_port(host, port)
            status = "OPEN" if is_open else "closed"
            print(f"Port {port:5d}: {status}")

            # Ethical scanning: delay to avoid hammering host
            time.sleep(0.05)

    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.")
    except socket.timeout:
        print("[ERROR] Connection timed out.")
    except KeyboardInterrupt:
        print("\n[INFO] Scan interrupted by user.")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
    finally:
        print(f"\n[INFO] Scan ended at: {datetime.now()}")
        print("[INFO] Port scanner finished.")


if __name__ == "__main__":
    main()
