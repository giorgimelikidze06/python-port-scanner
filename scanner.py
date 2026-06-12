import socket
import sys
import concurrent.futures
from datetime import datetime

open_ports = []

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        s.close()
    except KeyboardInterrupt:
        sys.exit()
    except Exception:
        pass

def main():
    print("-" * 50)
    print("Mini Port Scanner")
    print("-" * 50)
    
    target = input("Enter target IP (e.g., 127.0.0.1 for localhost): ")
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    print(f"\nScanning Target: {target_ip}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, target_ip, port)
            
    print("-" * 50)
    print("Scan completed.")
    
    
    if open_ports:
        print("\nSaving results to file...")
        with open("scan_results.txt", "w") as file:
            file.write(f"Scan results for IP: {target_ip}\n")
            file.write(f"Time: {datetime.now()}\n")
            file.write("-" * 30 + "\n")
            
            for p in sorted(open_ports):
                file.write(f"Port {p} is OPEN\n")
        print("[v] Results successfully saved in 'scan_results.txt'")
    else:
        print("\nNo open ports found to save.")

if __name__ == "__main__":
    main()