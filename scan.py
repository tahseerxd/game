import socket
import os

# Set up color codes
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
end = '\033[0m'

# Print header
print(f"{yellow}==================================================")
print("          PORT SCANNER - By Tabish M.")
print("==================================================\n")
print("Please select the type of scan you'd like to perform:\n")

# Print options
print(f"{yellow}[1] TCP")
print("[2] UDP")
print("[3] Game Ports{end}\n")

# Get user input for scan type
scan_type = input("Enter selection: ")

# Get target IP address from user
target = input("\nEnter target IP address: ")

# Set up color code for selected scan type
if scan_type == '1':
    scan_color = green
    protocol = 'TCP'
elif scan_type == '2':
    scan_color = red
    protocol = 'UDP'
elif scan_type == '3':
    scan_color = yellow
    protocol = 'Game Ports'

# Print scan type and target IP address
print(f"\nScanning for {scan_color}{protocol}{end} on {target}...\n")

# Set up list of common game ports
game_ports = [27015, 27016, 27017, 7777, 7778, 7779, 7780, 7781, 7782, 7783, 27960, 28960]

# Loop through ports and check if they are open
for port in range(1, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((target, port))
    if result == 0:
        if int(port) in game_ports:
            service = "Game Port"
        else:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
        print(f"{green}[+] Port {port} is open ({service}){end}")
    else:
        print(f"{red}[-] Port {port} is closed{end}")
    s.close()

# Print completion message
print(f"\n{yellow}Scan complete!{end}")
