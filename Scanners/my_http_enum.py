"Given Target IP/Domain + Port Enum HTTP methods of OPTION is allowed."
import http.client

TARGET = input("Target URL/IP: ")
PORT = input("Target Port(default 80): ")


if PORT == "":
    PORT = 80

try:
    conn = http.client.HTTPConnection(TARGET, PORT, timeout=10)
    conn.request("OPTIONS", '/')
    res = conn.getresponse()
    print(f"Allowed Methods are: {res.getheader('allow')}")
    conn.close()
except ConnectionRefusedError:
    print("Connection Failed")
