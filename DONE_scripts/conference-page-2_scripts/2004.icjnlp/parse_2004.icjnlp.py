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
from common import remove_parenthesised, remove_digit, remove_page, has_pp, extract_pages
import re
import csv
import spacy
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# save webpage

FILE_NAME = sys.argv[0]
FILE_NAME = FILE_NAME.split("_")[1].replace(".py", "")
print(FILE_NAME)
URL = get_url(FILE_NAME, conference_page=2)
save_page(URL, FILE_NAME)  # Uncomment the first time you run this script

with open(FILE_NAME, 'rb') as g:
    html = g.read()
bs = BeautifulSoup(html, "html.parser")
page_lines = bs.find_all(['p'])


nlp = spacy.load("en_core_web_sm")
track = None
vol=None
abstract=None
pages=None
pdf=None
presentation=None
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name", "Pages", "Abstract", "Notes"])
                     
    for i in range(len(page_lines)-2):
        j = 1
        p = page_lines[i]
        p1 = page_lines[i+1]

        if is_subtitle(p):
            track = is_subtitle(p)
            track = unspace(track)
            continue
        authors=None
        if has_pp(p):
            pages=extract_pages(p)
            print(pages)

        else:
            continue
        title_authors = p.get_text().split(":")[1].split("–")
        title = unspace(title_authors[0])
        authors = title_authors[1]
        authors = remove_parenthesised(authors)
        authors = namify(authors)
        abstract = p1.text

        line = [title, authors, pdf, presentation, vol, pages, abstract, track]
        writer.writerow(line)
