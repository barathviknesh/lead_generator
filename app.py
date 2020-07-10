import requests
import urllib.request
from bs4 import BeautifulSoup

# get url as input and return the html content (table)


def get_webpage(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find('table', {'class': 'table100'})
    return tables


url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html"


print(get_webpage(url))
