# -*- coding: utf-8 -*-
"""

This script is an example of how to generate a tsv file from an mt-archive conference page.
NOTE: 
-Make sure the conferenceList.csv file is present in the parent folder
-The name of the script is important, make sure to have the code of the conference between a '_' and the '.py'
 extention for instance: parse_2002.amta.py
-Make sure the common.py file is present in the same or the parent folder.

Author: Marie Dubremetz

"""
import sys
sys.path.append('..')
from common import save_page, get_url, is_subtitle, has_pdf, namify, get_title, has_italic, unspace, is_centered, has_bold
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import spacy
import csv
import re
from common import remove_parenthesised, remove_digit, remove_page, has_pp, extract_pages, has_bold



# save webpage

FILE_NAME = sys.argv[0]
FILE_NAME = FILE_NAME.split("_")[1].replace(".py", "")
print(FILE_NAME)

with open(FILE_NAME, 'r') as g:
    page_lines = g.readlines()


nlp = spacy.load("en_core_web_sm")
track = None
vol = None
abstract = None
pages = None
pdf = None
presentation = None
title = []
pages_in_pdf = None
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name", "Pages", "pages in pdf", "Notes"])

    for i in range(len(page_lines)):
        p = page_lines[i]
        p1 = page_lines[i+1]
        p2 = page_lines[i+2]
        title=unspace(p1)
        authors=unspace(p2)
        pages=unspace(p)
        try:
            pages=extract_pages(p)
        except:
            print(p1)
            continue
        
        title=unspace(title)


        authors = unspace(authors)
        authors = namify(authors)
        vol=unspace("""Vol.2:
Commercial MT Users and Translators Track
Government MT Users Track""")
        
        pages_in_pdf = str(int(pages)+7)
        if len(title) < 4:
            continue
        line = [title, authors, pdf, presentation,
                vol, pages, pages_in_pdf, track]
        writer.writerow(line)
