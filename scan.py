import socket
import sys
import os

# Define colors for output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Define dictionary of game ports and their associated games
game_ports = {
    80: 'Quake 3',
    6112: 'Diablo 2',
    7777: 'Unreal Tournament',
    8888: 'Unreal Tournament',
    27960: 'Return to Castle Wolfenstein',
    20560: 'Aliens vs. Predator',
    20561: 'Aliens vs. Predator',
    8767: 'TeamSpeak',
    27015: 'Half-Life',
    27016: 'Half-Life',
    27017: 'Half-Life',
    27018: 'Half-Life',
    27019: 'Half-Life',
    28960: 'Call of Duty',
    29900: 'Steam',
    29901: 'Steam',
    29920: 'Steam',
    17475: 'Minecraft',
    25565: 'Minecraft'
}

# Clear screen and print header
os.system('cls' if os.name == 'nt' else 'clear')
print(bcolors.HEADER + '------------------------------------------------------')
print('            GAME PORT SCANNER FOR HOSTS')
print('------------------------------------------------------\n' + bcolors.ENDC)

# Ask user for target host or IP
target_host = input('Enter target host or IP address: ')

# Create a TCP socket object
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.settimeout(1.0)

# Create a UDP socket object
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.settimeout(1.0)

# Loop through game ports and check if they're open
for port, game in game_ports.items():
    try:
        # Check if TCP port is open
        tcp_result = tcp_sock.connect_ex((target_host, port))
        if tcp_result == 0:
            print(f'{bcolors.OKGREEN}[+] Port {port} ({game}) is open.{bcolors.ENDC}')

        # Check if UDP port is open
        udp_sock.sendto(b'hello', (target_host, port))
        udp_result = udp_sock.recvfrom(1024)
        if udp_result:
            print(f'{bcolors.OKGREEN}[+] Port {port} ({game}) is open.{bcolors.ENDC}')

    except:
        # Print error if any exception is raised
        print(f'{bcolors.FAIL}[-] Port {port} ({game}) is closed.{bcolors.ENDC}')

# Close sockets
tcp_sock.close()
udp_sock.close()
