import argparse
import socket
from concurrent.futures import ThreadPoolExecutor

def tcp_scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        print(f"TCP Port {port} is open")
        s.close()
    except:
        pass

def udp_scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        s.sendto(b"", (host, port))
        _ = s.recvfrom(1024)
        print(f"UDP Port {port} is open")
        s.close()
    except:
        pass

def scan_ports(host, start, end, proto):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start, end):
            if proto == "tcp":
                executor.submit(tcp_scan, host, port)
            elif proto == "udp":
                executor.submit(udp_scan, host, port)

def main():
    parser = argparse.ArgumentParser(description="Port scanner tool", usage="%(prog)s ipv4")
    parser.add_argument("ipv4", type=str, help="IPv4 address to scan")

    args = parser.parse_args()

    host = args.ipv4
    print(f"Scanning TCP and UDP ports for {host}")

    print("Scanning TCP ports...")
    scan_ports(host, 0, 65536, "tcp")

    print("Scanning UDP ports...")
    scan_ports(host, 0, 65536, "udp")

if __name__ == "__main__":
    main()
