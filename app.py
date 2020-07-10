import requests
# import urllib.request
from bs4 import BeautifulSoup
# from parse import compile
# get url as input and return the html content (table) or (none) if url not exist

# first ########################################################################################################################################################3


def get_webpage(url):
    try:
        r = requests.get(url)
        page = r.text

        return page
    except:
        return None

# get html to string

# secound ###########################################################################################################################################################3


def get_webpage_text(html_web):
    sou = BeautifulSoup(html_web, "lxml")
    page_contents = sou.text
    return page_contents

# third ###############################################################################################################################################################


def get_list(html_web):
    soup = BeautifulSoup(html_web, "lxml")
    source = soup.findAll('a', {'class': '100link'})
    # empty array initiated for companys
    company_list = []
    for x in source:
        if x.text != "View From The Top Profile":
            company_list.append([x.text, x.get('href')])
    return company_list


#fourth #################################################################################################################################################################
    # url
url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html"


# checking purpose #####################################################################################################################################################
# first
html_web = get_webpage(url)
# print(html_web)
# secound
web_pages1 = get_webpage_text(html_web)
# print(web_pages1)
# third
companysL = get_list(html_web)
print(companysL)
