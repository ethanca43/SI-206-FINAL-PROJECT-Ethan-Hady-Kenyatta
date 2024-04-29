from bs4 import BeautifulSoup
import os
import re


# div trackList g-all-transitions-300 lazyLoadingList

# ul 
# li



def scrap(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)
    with open(full_path, mode = 'r', encoding ="utf-8-sig") as openfile:
         #print(openfile)
         data = openfile.read()
         nl = []
         #print(data)

         soup = BeautifulSoup(data, 'html.parser')
         get_span= soup.find_all("span", class_="sc-ministats")
         print(get_span[0].text)


scrap('soundcloud_html/Greedy_ArianaGrande.html')

scrap('soundcloud_html/Adele_rollinginthedeep.html')
