"""Port scanner for IPv4 targets uses connect_ex()

description: Basic + extremely slow (no threading) port scanner that loops throu giving port rang.
Input: Target IPv4 + range of ports
Return: open ports for given Target
"""

import socket

TARGET_ADDRESS = input("Target IPv4: ")
PORT_RANGE = input("range of ports to scan (ex. 1-400): ")

MIN_PORT = int(PORT_RANGE.split('-')[0])
MAX_PORT = int(PORT_RANGE.split('-')[1])

print(f"Scanning {TARGET_ADDRESS} from {MIN_PORT} to {MAX_PORT}")

li_open_ports = []
for PORT in range(MIN_PORT, MAX_PORT + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex((TARGET_ADDRESS, PORT))
        li_open_ports.append(PORT)
        print(f"port: {PORT} open")
    except Exception:
        print(f"port: {PORT} CLOSED")
        continue
    s.close()


if len(li_open_ports) > 0:
    print(f"Target: {TARGET_ADDRESS} have these ports open: {li_open_ports}")
    print(f"there were {len(li_open_ports)} ports open in the specified rang {PORT_RANGE}")
else:
    print(f"couldn't find open ports for{TARGET_ADDRESS} in specified range {PORT_RANGE}")
