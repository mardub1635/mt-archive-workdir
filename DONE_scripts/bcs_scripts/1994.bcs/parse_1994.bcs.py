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
from common import remove_parenthesised
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

        #get the track
        if is_centered(p):
            print("New track name:", track)
            # track = is_centered(p)
            

            continue

        raw_text = unspace(p.get_text())
        pdf = None
        title=None
        if has_pdf(p):
            pdf = has_pdf(p)
            pdf = urljoin(URL, pdf)
            #print(pdf)

        presentation = None
        if "presentation" in p.text:
            presentation = has_pdf(p)
            presentation = urljoin(URL, presentation)
        try:
            # Remove the first text before ":"
            if pdf:
                title = get_title(p)
        except:
            continue

        authors = p.text.split(":")[0]
        authors = namify(authors)
        if len(authors) <= 2 and title == None:
            continue
        if title == None:
            try:
                title = p.text.split(":")[1]
            except:
                pass
        try:
            title = unspace(title)
            title = remove_parenthesised(title)
        except:
            pass
        line = [title, authors, pdf, presentation, vol, track]
        writer.writerow(line)
