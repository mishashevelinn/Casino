from bs4 import BeautifulSoup
from selenium import webdriver
import requests


html_string = requests.get("https://magicseaweed.com/Backdoor-Haifa-Surf-Report/3987/").content
soup = BeautifulSoup(html_string, "html.parser")

lower_weekly = []
higher_weekly = []
ais=[]
for a in soup.findAll('span', attrs={'class':'h3 font-sans-serif heavy nomargin text-white'}):


    lower_weekly.append(a.contents[0])
    if len(a) < 4:
        higher_weekly.append(a.contents[0])
    else:
        higher_weekly.append(a.contents[2])

reports = []
reports_len = len(higher_weekly)
for a in soup.findAll('ul', attrs={'class':'rating clearfix'}):
    ais.append(a)
print(reports_len)
print(len(ais))
stars = []
for k in ais:
    stars.append(str(k).count('active'))
print(stars)



# for i in range(reports_len):
#     for j in ais[i]:
