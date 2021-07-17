"""
    Client that starts a conn to my other python server(my_socket.py)
    & sends a  message.
"""
import socket

SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((SRV_ADDR, SRV_PORT))
print("Connection Established...")

while 1:
    msg = input("Send this: ")
    s.sendall(msg.encode())
    data = s.recv(1024)  #? to rec respond from the server and print it to me
    print(data.decode('utf-8'))

s.close()


