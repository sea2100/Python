import re
from bs4 import BeautifulSoup as BS

with open ("index.html",'r', encoding='UTF-8') as f:
    s=f.read()
print (re.findall('<span class="total-users">([^\"]+)</span>',s))
soup=BS(s,'html.parser')
print (soup.find('span').string)
