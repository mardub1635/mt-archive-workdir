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
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name", "Notes"])

    for p in page_lines:
        authors=None
        #get the track
        if has_bold(p):
            print("New track name:", track)
            track = has_bold(p)

            continue

        raw_text = unspace(p.get_text())
        pdf = None

        if has_pdf(p):
            pdf = has_pdf(p)
            pdf = urljoin(URL, pdf)
            #print(pdf)

        presentation = None
        try:
            # Remove the first text before ":"
            title = get_title(p)
        except:
            continue
        text=unspace(p.get_text())
        if text[1]==".":
            authors=text.split(",")[0]
        try:
            title=text.split(":")[0]
            authors=text.split(":")[1].split(",")[0]
        except:
            pass
        #authors = namify(authors)
        
        line = [title, authors, pdf, presentation, vol, track]
        writer.writerow(line)
