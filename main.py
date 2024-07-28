import requests
import json
from bs4 import BeautifulSoup

months={"Ocak":31,"Şubat":29,"Mart":31,"Nisan":30,"Mayıs":31,"Haziran":30,"Temmuz":31,"Ağustos":31,"Eylül":30,"Ekim":31,"Kasım":30,"Aralık":31}

for month,day_count in months.items():
    for i in range(1,day_count+1):
        url="https://tr.wikipedia.org/wiki/{}_{}".format(i,month)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        eventsList = [child.get_text() for child in soup.find("ul",{"class":""}).children]
        eventsList.reverse()
        json_event_list=json.dumps(eventsList)
        file_name = month+"/"+str(i)+".json"
        f = open(file_name, 'w+')  # open file in write mode
        f.write(json_event_list)
        f.close()
        
