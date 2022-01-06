import requests
from bs4 import BeautifulSoup

def get_password_list_from_wiki():

    url = 'https://en.wikipedia.org/wiki/List_of_the_most_common_passwords'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    td = soup.find_all('td', align="left")

    password_list = []
    for item in td:
        password_list.append(item.text.replace("\n", "").replace("[a]", ""))

    return list(set(password_list))