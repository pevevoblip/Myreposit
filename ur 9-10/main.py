import urllib.request
from http.client import responses

import requests
from urllib3 import request
from bs4 import BeautifulSoup
'''
opener = urllib.request.build_opener()

response = requests.get('https://httpbin.org/get')

print(response.content())
print(f'Datatype {type(response.content)}')
'''

response = requests.get('https://coinmarketcap.com/')
'''
response_text = response.text

response_pars = response_text.split("<span>")

coins_data = []

for parse_elem1 in response_pars:
    if parse_elem1.startswith("$"):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2.startswith("$") and parse_elem2[1].isdigit():
                print(parse_elem2)


print("BTC" + '-' + coins_data[0])

'''

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", )