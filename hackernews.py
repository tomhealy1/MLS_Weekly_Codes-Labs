import requests

import requests

url = "https://hacker-news.firebaseio.com/v0/item/8863.json?"

payload={}
files={}
headers = {
  'Accept': 'application/json',
  }

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)