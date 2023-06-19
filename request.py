from bs4 import BeautifulSoup
from requests import *
import requests
request = requests.get('https://vnexpress.net')
print(request.text)
