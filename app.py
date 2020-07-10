import requests  # _________________________ REFERENCE ATTACHED AT END__________________##########################################################
# import urllib.request
from bs4 import BeautifulSoup
# from parse import compile
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

#five#######

# def get_location(text : str)-> list:
# """
# : Param text: visible webpage text from get_webpage_text function
# :return: list of extracted addresses from a given text
# """

#six###########

# def save_to_json(filename : str ,json_dict : dict)-> None:
# """
# : Param filename: file name for the json file
# : Param json_dict: dictionary file - {"company1:",["address1"]....}
# :return: None
# """

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

  #for my reference ######################

# Opening JSON file and loading the data
# into the variable data
with open('data.json') as json_file:
    data = json.load(json_file)

employee_data = data['emp_details']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in employee_data:
    if count == 0:

        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

data_file.close()

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


# reference##########################^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#####################################
# http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
# https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
# https://stackoverflow.com/questions/16322862/beautiful-soup-findall-doesnt-find-them-all
