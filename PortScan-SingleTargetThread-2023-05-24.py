import sys
import socket
import threading
from queue import Queue

# Function to perform the port scan
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Function to handle multi-threading
def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

# Function to display usage information
def show_usage():
    print("Port Scan Tool")
    print("Usage: python portscan.py <IPv4 address>")
    print("Example: python portscan.py 127.0.0.1")

# Main function
def main(argv):
    global target_ip, q
    if len(argv) == 2:
        if argv[1].lower() == "-h":
            show_usage()
            sys.exit()

        target_ip = argv[1]
        q = Queue()

        # Create threads
        for _ in range(100):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        # Scan ports 1 to 65535
        for worker in range(1, 65536):
            q.put(worker)

        q.join()
    else:
        show_usage()
        sys.exit()

if __name__ == "__main__":
    main(sys.argv)
