import requests  # _________________________ REFERENCE ATTACHED AT END__________________########################################################################
# import urllib.request
from bs4 import BeautifulSoup
# from parse import compile
import re
import json
import csv
# get url as input and return the html content (table) or (none) if url not exist

# first ########################################################################################################################################################


def get_webpage(url):
    try:
        r = requests.get(url)
        page = r.text

        return page
    except:
        return None

# get html to string

# secound ###########################################################################################################################################################


def get_webpage_text(inputs):
    sou_one = BeautifulSoup(inputs, "lxml")
    page_contents = sou_one.text
    return page_contents

# third ###############################################################################################################################################################


def get_list(inputstwo):
    soup_2 = BeautifulSoup(inputstwo, "lxml")
    source = soup_2.findAll('a', {'class': '100link'})
    company_list = []
    for x in source:
        if x.text != "View From The Top Profile":
            company_list.append([x.text, x.get('href')])
    return company_list


#fourth #################################################################################################################################################################


# def get_contact_page_link(html : str )-> list:
# """
# : Param html: html output from get_webpage function
# :return: list of internal links that have "contact" / "about". Type- List
# """


def get_contact_page(inputsthree):
    company_name_url_list = get_list(inputsthree)
    contact_list = []
    for list_in in company_name_url_list[:10]:
        try:
            # fro fetch company name
            company_Name = list_in[0]
            # for fetch
            company_url = list_in[1]
            company_pg = get_webpage(company_url)
            souper = BeautifulSoup(company_pg, 'lxml')
            source = souper.findAll('a')
# the about key word is used for search #################3
            test_case_one = ["contact"]
            for it_s in source:
                for x in test_case_one:
                    # search with key word
                    if re.search(x, it_s.get('href')):
                        if it_s.get('href').startswith('http'):
                            contact_list.append(
                                [company_Name, it_s.get('href')])
                        else:
                            contact_list.append(
                                [company_Name, company_url+it_s.get('href')])
        except:
            print(company_Name, company_url)
            # pass
    groups = []
    [groups.append(it_s)
     for it_s in contact_list if it_s not in groups]

    return groups
    #five#######

    # def get_location(text : str)-> list:
    # """
    # : Param text: visible webpage text from get_webpage_text function
    # :return: list of extracted addresses from a given text
    # """

# attempt one
# def get_location(html_web):
#     # textfun = html_web

#     extract = BeautifulSoup(html_web, "html.parser")
#     location = extract.findAll('p', {'class': 'address'})
#     locality = []
#     for xadr in location:
#         locality.append([xadr])
#         print(xadr)
#     return locality


def get_location(inputsix):
    patterns = [r'^[0-9]{2} .\n.\n.*\n', r'^[0-9]{4} .\n.\n.*\n',
                r'^[0-9a-zA-Z ]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]{5}\n\bUnited States|USA\b$', r'^[0-9]{3}[a-z|A-Z\s]*\s[a-z|A-Z]{2}.[A-Z|a-z]*\s[0-9]*[A-z|a-z|0-9]*[,]\s[A-Z]{2}\s[0-9]{5}$', r'^[a-z|A-Z|0-9]*[,]\s[A-z]{2}\s[0-9]{5}\r\n\bUnited States\b', r'[0-9]*\s[A-z].\s[a-z|0-9]*\s[A-Z|a-z]*.\n[A-Za-z]*\s[A-z|a-z]*[, ]\s[A-Z]{2}\s[0-9]{5}\n\bUSA\b']
    rough_li = []
    for pattern in patterns:
        extrated = re.findall(pattern, inputsix.strip(), flags=re.MULTILINE)
        for item in extrated:
            item = re.sub(r'[^\x00-\x7f]', ' ', item)
            item = re.sub(r'\n|\t|\r', ' ', item)
            rough_li.append(item)
    fair_li = []
    fair_li = [
        adr for adr in rough_li if adr not in fair_li]
    return fair_li

    #six###########


# list to json file


# checking purpose #####################################################################################################################################################

# url
url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html"
# url = "https://www.acquia.com/about-us/contact"


# first
first = get_webpage(url)
# print(first)

# secound
secound = get_webpage_text(first)
# print(secound)

# third
third = get_list(first)
# print(third)

# four
fourth = get_contact_page(first)
# print(fourth)

# reference##########################^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#####################################
# http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
# https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
# https://stackoverflow.com/questions/16322862/beautiful-soup-findall-doesnt-find-them-all

if __name__ == "__main__":
    # first
    first = get_webpage(url)
    # print(first)
    # secound
    secound = get_webpage_text(first)
    # print(secound)
    # third
    third = get_list(first)
    # print(third)
    # four
    fourth = get_contact_page(first)
    # print(fourth)
    ### or else plz print in see output ###
