import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in"
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
title=soup.title
print("title of the webpage: ",title.text)
print(soup.li)