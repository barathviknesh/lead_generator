import requests
import urllib.request
from bs4 import BeautifulSoup
# from parse import compile
# get url as input and return the html content (table)


def get_webpage(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find('table', {'class': 'table100'})
    return tables

# get html to string


def get_webpage_text(html_table):
    htmlToxml = html_table
    webpagetxt = htmlToxml.text
    return webpagetxt


url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html"

# table stored in variable
html_table = get_webpage(url)

# html saved as txt in variable
html_table_txt = get_webpage_text(html_table)

print(html_table_txt)
