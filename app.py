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


def get_webpage_text(html_web):
    sou_one = BeautifulSoup(html_web, "lxml")
    page_contents = sou_one.text
    return page_contents

# third ###############################################################################################################################################################


def get_list(html_web):
    soup_2 = BeautifulSoup(html_web, "lxml")
    source = soup_2.findAll('a', {'class': '100link'})
    # empty array initiated for companys
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


def get_contact_page(companysL):
    company_name_url_list = get_list(html_web)
    contact_list = []
    for list_in in company_name_url_list:
        try:
            # fro fetch company name
            company_Name = list_in[0]
            # for fetch
            company_url = list_in[1]
            company_pg = get_webpage(company_url)
            souper = BeautifulSoup(company_pg, 'lxml')
            source = souper.findAll('a')
# the about key word is used for search #################3
            test_case_one = ["about"]
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


def get_location(html_web):
    # textfun = html_web

    extract = BeautifulSoup(html_web, "html.parser")
    location = extract.findAll('p', {'class': 'address'})
    locality = []
    for xadr in location:
        locality.append([xadr])
        print(xadr)
    return locality

    #six###########


# list to json file
# listw = [1, 2, 3, 4, 5, 6, 7]


# def save_to_json(listw):
#     with open(listw, "w") as file_obj:
#         file_obj.write(json.dumps(listw))
    # def save_to_json(filename : str ,json_dict : dict)-> None:
    # """
    # : Param filename: file name for the json file
    # : Param json_dict: dictionary file - {"company1:",["address1"]....}
    # :return: None
    # """

    # yet to be done

    #seven#########

    # def json_to_csv_file(json_filename  : str ,csv_filename : str)-> None:
    # """
    # : Param json_filename: file name for the json file
    # : Param csv_filename: file name for the csv file
    # Company | Addresses
    # :return: None
    # """
    # Python program to convert
    # JSON file to CSV
    # yet to be done
    # for my reference ###################### yet to be done *
    # Opening JSON file and loading the data
    # into the variable data
    # now we will open a file for writing
    # create the csv writer object
    # Counter variable used for writing
    # headers to the CSV file
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
# fourth
# four = get_contact_page(companysL)
# print(four, print("fourrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"))
# five
lock = get_location(html_web)
# print(lock)
# reference##########################^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#####################################
# http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
# https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
# https://stackoverflow.com/questions/16322862/beautiful-soup-findall-doesnt-find-them-all
if __name__ == "__main__":
    html_web = get_webpage(url)
    web_pages1 = get_webpage_text(html_web)
    companysL = get_list(html_web)
    lock = get_location(html_web)
 ### or else plz print in see output ###
