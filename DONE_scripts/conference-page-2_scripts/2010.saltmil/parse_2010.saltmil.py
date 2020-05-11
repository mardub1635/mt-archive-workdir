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
from common import save_page, get_url, is_subtitle, has_pdf, namify, get_title, has_italic,unspace, is_centered, has_bold
from common import remove_parenthesised, remove_digit, remove_page, has_pp, extract_pages, has_bold
import re
import csv
import spacy
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# save webpage

FILE_NAME = sys.argv[0]
FILE_NAME = FILE_NAME.split("_")[1].replace(".py", "")
print(FILE_NAME)

with open(FILE_NAME, 'r') as g:
    page_lines = g.readlines()


nlp = spacy.load("en_core_web_sm")
track = None
vol=None
abstract=None
pages=None
pdf=None
presentation=None
title=[]
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name", "Pages", "Notes"])
                     
    for string_line in page_lines:
        
        title_authors_pages = string_line.split("\"")
        
        try:
            authors = title_authors_pages[1]
        except:
            track=unspace(string_line)
            continue
        authors=remove_parenthesised(authors)
        authors=remove_page(authors)
        authors=unspace(authors)
        authors = namify(authors)

        title = title_authors_pages[0]
        pages = title_authors_pages[1]
        pages = extract_pages(pages)
        if len(title) < 4:
            continue
        line = [title, authors, pdf, presentation, vol, pages, track]
        writer.writerow(line)
