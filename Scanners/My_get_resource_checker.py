"Given Target IP/Domain + Port check if given resource exsits using GET method."
import http.client
from colorama import init, Fore, Back, Style

init()

TARGET = input("Target URL/IP: ")
PORT = input("Target Port(default 80): ")


if PORT == "":
    PORT = 80

print("------------establishing connection-----------")
try:
    conn = http.client.HTTPConnection(TARGET, PORT, timeout=10)
    conn.request("GET", '/')

    res = conn.getresponse()
    if str(res.status)[0] == "2":
        print(Fore.GREEN + f"Status: {res.status} and reason: {res.reason}")
    else:
        print(Fore.RED + f"Status: {res.status} and reason: {res.reason}")

    headers = res.getheaders()
    for header, content in headers:
        print(Fore.LIGHTMAGENTA_EX + f"{header} : " + Fore.BLUE + f"{content}")

    conn.close()
except ConnectionRefusedError:
    print("Connection Failed")
