# importing the requests library
import requests
from xml.etree import ElementTree
from datetime import datetime

print(datetime.now().year)
print(datetime.now().month)

print(datetime.now().day)
print(datetime.now().hour)

now = datetime.now()
year = now.year - 2000
month = now.month if now.month >= 9 else f"0{now.month}"
day = now.day if now.day >= 9 else f"0{now.day}"
hour = now.hour if now.hour >= 9 else f"0{now.hour}"

api_date = f"{year}{month}{day}"
api_hour = f"{hour}"
  
# api-endpoint
URL = f"https://api.deutschebahn.com/timetables/v1/plan/8011160/{api_date}/{api_hour}"
  
# defining a params dict for the parameters to be sent to the API
headers = {"Authorization": "Bearer dec0445e9c29bf5bc4e8c1641c6ba1fc"}
  
# sending get request and saving the response as response object
print("Making request.")
r = requests.get(url = URL, headers=headers)
print("Request status code:", r.status_code)
  
# extracting data in json format
data = ElementTree.fromstring(r.content)
 

for k in data:
    for l in k:
        if l.tag == 'ar':
            if 'cp' in l.attrib or 'ct' in l.attrib:
                print(k.tag, k.attrib, l.tag, l.attrib)
        if l.tag == 'dp':
            if 'cp' in l.attrib or 'ct' in l.attrib:
                print(k.tag, k.attrib, l.tag, l.attrib)            