# -*- coding: utf-8 -*-
"""

This script is an example of how to generate a tsv file from an mt-archive conference page.
NOTE: 
-Make sure the conferenceList.csv file is present in the parent folder
-The name of the script is important, make sure to have the code of the conference between a '_' and the '.py'
 extension for instance: parse_2002.amta.py
-Make sure the common.py file is present in the same or the parent folder.

Author: Marie Dubremetz

"""
import sys
sys.path.append('..')
from common import save_page, get_url, is_subtitle, has_pdf, namify, get_title, has_italic,unspace, remove_parenthesised
from common import extract_pages
import re
import csv
import spacy
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# save webpage

FILE_NAME = sys.argv[0]
FILE_NAME = FILE_NAME.split("_")[1].replace(".py", "")
print(FILE_NAME)
URL = get_url(FILE_NAME)
save_page(URL, FILE_NAME)  # Uncomment the first time you run this script

with open(FILE_NAME, 'rb') as g:
    html = g.read()
bs = BeautifulSoup(html, "html.parser")
page_lines = bs.find_all(['p'])


nlp = spacy.load("en_core_web_sm")
track = None
presentation=None
vol=None
pages=None
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name","Pages" ,"Notes"])

    for i in range(len(page_lines)):
        j = 1
        p = page_lines[i]
        p1 = page_lines[i+1]
        


        raw_text = p.get_text().replace("\n", " ")
        
        pdf = None
        authors=None
        if "(" in p.text :
            authors=is_subtitle(p)
            if "(" in p1.text :
                try:
                    authors = authors+", "+is_subtitle(p1)
                except:
                    continue
                p2 = page_lines[i+2]
                j = 2
                p1 = p2

        else:
            continue

        if authors==None:
            continue
        title=p1.text
        track=None
        if "abstract" in title:
            track= "abstract"
        title=remove_parenthesised(title)

        while len(p1.text.strip()) <= 3:
            p1 = page_lines[i+j]
            j = j+1
        try:
            pages = extract_pages(p)
        except:
            pass
        pdf=has_pdf(p1)
        pdf = urljoin(URL, pdf)
        print(authors)
        authors=remove_parenthesised(authors)
        authors = namify(authors)

        title = unspace(title)
        line = [title, authors, pdf, presentation, vol,pages, track]
        writer.writerow(line)
