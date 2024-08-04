import requests
import json
from pathlib import Path

from bs4 import BeautifulSoup

class Month:
    def __init__(self, name,day_count):
        self.name=name
        self.day_count=day_count

months=[Month("Ocak",31),Month("Şubat",29) ,Month("Mart",31),Month("Nisan",30),Month("Mayıs",31),Month("Haziran",30),Month("Temmuz",31),Month("Ağustos",31),Month("Eylül",30),Month("Ekim",31),Month("Kasım",30),Month("Aralık",31)]

for month_idx in range(len(months)):
    month=months[month_idx]
    for i in range(1,month.day_count+1):
        url="https://tr.wikipedia.org/wiki/{}_{}".format(i,month.name)
        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8','ignore'), 'html.parser')
        eventsList = [str(child.get_text()) for child in soup.find("ul",{"class":""}).children if child.get_text()!='\n']
        eventsList.reverse()
        json_event_list=json.dumps(eventsList,ensure_ascii=False)
        Path(str(month_idx)).mkdir(parents=True, exist_ok=True)
        file_name = str(month_idx)+"/"+str(i)+".json"
        f = open(file_name, 'w+',encoding='utf-8')  # open file in write mode
        f.write(json_event_list)
        f.close()
        
