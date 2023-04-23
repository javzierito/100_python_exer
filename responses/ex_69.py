import requests
 
headers = {'User-agent': 'Mozilla/4.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
# we are trying to import from an empty file, therefore is not going to work. even more it may conflict with the module requests
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:99])