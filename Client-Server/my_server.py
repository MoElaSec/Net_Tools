# eLearnSecurity 2013

import socket

SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)  # ? sspecifies max num of queued connections.
print("Server started! Waiting for connections...")
connection, address = s.accept()  # ? conn -> socket obj used to send/rec data, address -> client add bound to the socket.
print('Client connected with address:', address)

while 1:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))

connection.close()
