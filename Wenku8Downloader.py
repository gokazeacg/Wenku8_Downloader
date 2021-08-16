import requests
import wget
import os
from bs4 import BeautifulSoup

num = input('輸入小說id：')
id = str(num)
ids = int(id)
response = requests.get("https://www.wenku8.net/book/"+num+".htm")
response.encoding = 'gbk'
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
titles = soup.find_all("b")
#print(len(str(titles[2])))
titlelong = len(str(titles[2]))
title = str(titles[2])[3:titlelong-4]
print(title)
Ending = soup.find_all("td")
#print(Ending[5])
if str(Ending[5]) == '<td width="20%">文章状态：已完结</td>':
  print('已完結')
  a = 0
else:
  print('慢慢等吧')
  a = 1

if a == 0:
  if ids <= 1000:
    url = "http://dl.wenku8.com/txtbig5/0/"+num+".txt"
    location = "/content/"+num
    #print(url)
    os.system("wget"+" "+url+" "+"-O"+title+".txt")
  elif ids >= 3000:
    url = "http://dl.wenku8.com/txtbig5/3/"+num+".txt"
    location = "/content/"+num
    #print(url)
    os.system("wget"+" "+url+" "+"-O"+title+".txt")
  else:
    url = "http://dl.wenku8.com/txtbig5/2/"+num+".txt"
    location = "/content/"+num
    #print(url)
    os.system("wget"+" "+url+" "+"-O"+title+".txt")
else:
  print("尚未完結喔")