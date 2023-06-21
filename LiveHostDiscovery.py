import subprocess
import platform

def ping_ip(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response == 0

def read_ips_from_file(file_path):
    with open(file_path, "r") as file:
        ips = [line.strip() for line in file]
    return ips

def main():
    file_path = "ip_addresses.txt" # Replace this with the path to your text file
    ip_addresses = read_ips_from_file(file_path)

    for ip in ip_addresses:
        if ping_ip(ip):
            print(f"{ip} is alive")
        else:
            print(f"{ip} is not alive")

if __name__ == "__main__":
    main()