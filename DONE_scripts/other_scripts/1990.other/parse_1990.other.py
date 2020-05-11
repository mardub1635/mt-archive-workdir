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
from common import save_page, get_url, is_subtitle, has_pdf, namify, get_title, has_italic,unspace, is_centered
from common import remove_parenthesised, remove_page, extract_pages, has_bold
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
vol=None
pages=None
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name", "Pages", "Notes"])

    for p in page_lines:
        track = None
        try:
            
            pages = extract_pages(p)
            
        except:
            pass
        splitter = ":"
        line = unspace(p.text)
        sliced_line = line.split(splitter)
        try:
            left = sliced_line[0]

            right = ":".join(sliced_line[1:])
        except:
            print(sliced_line)
            continue

        raw_text = unspace(p.get_text())
        pdf = None
        title = None
        if has_pdf(p):
            pdf = has_pdf(p)
            pdf = urljoin(URL, pdf)
        title = right

        if "abstract" in p.text:
            track = "abstract"
        else:
            pass
        presentation = None
        if "presentation" in p.text:
            presentation=pdf
            pdf=None

        authors = p.text.split(":")[0]
        if title==None or authors==None:
            continue
        authors = namify(authors)
        if len(title) <= 3:
            continue


        try:
            title = unspace(unspace(title))
            
            
        except:
            pass
        #title= remove_page(title)
        print("page removed"+title)
            
            
        title= remove_parenthesised(title,exclude="(")
        line = [title, authors, pdf, presentation, vol, pages, track]
        writer.writerow(line)
