import requests
 
headers = {'User-agent': 'customUserAgent'}
r = requests.get("https://pythonhow.com/media/data/universe.txt", headers = headers)
print(r.text)