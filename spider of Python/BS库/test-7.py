'''
import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text

soup=BeautifulSoup(demo,"html.parser")
print(soup.prettify())
print("\n\n")
for parent in soup.p.parents:

      print(parent)
'''

import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text

soup=BeautifulSoup(demo,'html.parser')
for link in soup.find_all('p'):
      print(link.get('class'))
