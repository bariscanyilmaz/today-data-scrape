import re
import requests
import json
from pathlib import Path

from bs4 import BeautifulSoup

class Month:
    def __init__(self, name,day_count):
        self.name=name
        self.day_count=day_count

tr_months=[Month("Ocak",31),Month("Şubat",29) ,Month("Mart",31),Month("Nisan",30),Month("Mayıs",31),Month("Haziran",30),Month("Temmuz",31),Month("Ağustos",31),Month("Eylül",30),Month("Ekim",31),Month("Kasım",30),Month("Aralık",31)]
months=[Month("January",31),Month("February",29) ,Month("March",31),Month("April",30),Month("May",31),Month("June",30),Month("July",31),Month("August",31),Month("September",30),Month("October",31),Month("November",30),Month("December",31)]
pattern = r"\[\d+\]"

for month_idx in range(len(months)):
    month=months[month_idx]
    for i in range(1,month.day_count+1):
        url="https://en.wikipedia.org/wiki/{}_{}".format(month.name,i)
        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8','ignore'), 'html.parser')
        events_ul_list=soup.find_all("ul",{"class":""})[:3]
        eventsList = [str( re.sub(pattern, "", child.get_text())) for ul in map(lambda ul:ul,events_ul_list) for child in ul.children if child.get_text()!='\n']
        eventsList.reverse()
        json_event_list=json.dumps(eventsList,ensure_ascii=False)
        Path("en/"+str(month_idx)).mkdir(parents=True, exist_ok=True)
        file_name ="en/"+str(month_idx)+"/"+str(i)+".json"
        f = open(file_name, 'w+',encoding='utf-8')  # open file in write mode
        f.write(json_event_list)
        f.close()
        
