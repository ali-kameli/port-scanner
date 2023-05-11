import socket
import sys
import os
from colorama import Fore

if len(sys.argv) == 3:
    os.system('cls' or 'clear')
    ip = sys.argv[1]
    rangeOfPorts = sys.argv[2].split('-')

    print(f"""
{Fore.RED}
---------------------------------
[+_+] Target IP: {ip}
---------------------------------
{Fore.RESET} 
""")

    try:
        for port in range(int(rangeOfPorts[0]), int(rangeOfPorts[1])):
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = serverSocket.connect_ex((ip, port))

            if result == 0:
                print(f"{Fore.GREEN}port {port} is open !{Fore.RESET}")
    except KeyboardInterrupt:
        print(f"{Fore.RED}Scan Cancelled{Fore.RESET}")
    except socket.gaierror:
        print(f"{Fore.RED} Server NOT Responding{Fore.RESET}")
else:
    print('Invalid amount Arguments')
