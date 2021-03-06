#source from:https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,"html.parser")

print("I have token all links:\n")
links=soup.find_all('a')
for link in links:
	print(link.name,link['href'],link.get_text())

print("\nI will take the link of 'lacie':\n")
link1=soup.find('a',href="http://example.com/lacie")
print(link1.name,link1['href'],link1.get_text())


print("\nI will take the link of 'p':\n")
link2=soup.find('p',class_='title')
print(link2.name,link2.get_text())