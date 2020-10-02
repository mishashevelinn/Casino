from bs4 import BeautifulSoup
from tkinter import *
import time
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


reports_len = len(higher_weekly)
for a in soup.findAll('ul', attrs={'class':'rating clearfix'}):
    ais.append(a)


stars = []
for k in soup.find_all('td'):
    stars.append(str(k).count('active'))


conditions = [ ]
winds = []
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        if type(td.get('title')) == str:
            conditions.append(td.get('title'))


for i in conditions:
    if i.startswith('Light') or i.startswith('Very') or i.startswith('Moderate') or i.startswith('Gentle') or i.startswith('Fresh'):
        winds.append(i)


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

#GUI CODE STARDS HERE:
root = Tk()
frame = LabelFrame()