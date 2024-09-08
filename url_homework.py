import requests

url = 'https://www.google.com'


cont = requests.get(url)
if cont.status_code==200:
    print('url %s is active'%url)
else:
    print('url is inactive')    