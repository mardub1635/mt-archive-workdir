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
                     
    for line in page_lines:

        authors_title_page = line.replace("”", "“").split("“")
        authors = authors_title_page[0]
        authors = namify(authors)
        title = authors_title_page[1]
        pages = authors_title_page[2]
        pages = extract_pages(pages)
        line = [title, authors, pdf, presentation, vol, pages, track]
        writer.writerow(line)
