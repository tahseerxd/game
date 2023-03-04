import socket
import os

# Clear the terminal screen
os.system('clear')

# Define color codes for printing to the terminal
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Print welcome message and options to the terminal
print(f"{GREEN}{'='*30}\nWelcome to the Port Scanner!\n{'='*30}{RESET}\n")
print(f"{YELLOW}Please select the type of port scan you'd like to perform:\n{'-'*60}")
print(f"1) TCP Ports\n2) UDP Ports\n3) Gaming Ports\n{'-'*60}{RESET}")

# Get user input for the type of port scan to perform
scan_type = input(f"{YELLOW}Enter the number of the scan type you'd like to perform: {RESET}")

# Get the target IP address from the user
target_host = input(f"{YELLOW}Enter the IP address you'd like to scan: {RESET}")

# Define the port ranges to scan based on the user's selected scan type
if scan_type == '1':  # TCP Ports
    port_range = range(1, 65536)
    scan_name = 'TCP'
elif scan_type == '2':  # UDP Ports
    port_range = range(1, 65536)
    scan_name = 'UDP'
elif scan_type == '3':  # Gaming Ports
    port_range = [22, 80, 443, 27015, 27016, 27017, 27018, 27019, 28015, 28016, 28017, 28018, 28019, 28020]
    scan_name = 'Gaming'

# Clear the terminal screen
os.system('clear')

# Print the scan name and target IP address to the terminal
print(f"{GREEN}{'='*30}\n{scan_name} Port Scan Results for {target_host}\n{'='*30}{RESET}\n")

# Loop over the port range and attempt to connect to each port on the target IP address
for port in port_range:
    try:
        # Create a new socket and attempt to connect to the target IP address on the current port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if scan_type == '1' else socket.SOCK_DGRAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        
        # Print the port status and name to the terminal based on whether it's open or closed
        if result == 0:
            print(f"{GREEN}[+] {port}: Open - {get_service_name(port)}{RESET}")
        else:
            print(f"{RED}[-] {port}: Closed{RESET}")
        
        # Close the socket connection
        sock.close()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[*] User requested exit. Exiting...{RESET}")
        exit()
    except socket.gaierror:
        print(f"{RED}[-] Hostname could not be resolved. Exiting...{RESET}")
        exit()
    except socket.error:
        print(f"{RED}[-] Couldn't connect to server. Exiting...{RESET}")
        exit()
        
def get_service_name(port):
    if port == 22:
        return "SSH"
    elif port == 80 or port == 8080:
        return "HTTP"
    elif port == 443:
        return "HTTPS"
    elif port == 27015 or port == 27016 or port == 27017
