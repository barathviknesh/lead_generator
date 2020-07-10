import requests
import urllib.request
from bs4 import BeautifulSoup


def get_webpage(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find('table', {'class': 'table100'})
    return tables


url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html"

# r = requests.get(url)

# html_content = r.text

# soup = BeautifulSoup(html_content, "html.parser")
# tables = soup.find('table', {'class': 'table100'})
# print(tables)


print(get_webpage(url))
