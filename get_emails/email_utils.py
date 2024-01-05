import requests
import bs4
from bs4 import BeautifulSoup

website = 'https://mail.google.com'
response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
breakpoint()