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
from common import save_page, get_url, is_subtitle, has_pdf, namify, get_title, has_italic,unspace, remove_parenthesised, is_centered,has_bold
from common import remove_digit
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
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name","Notes"])

    for i in range(len(page_lines)-1):
        track=None

        p = page_lines[i]
        p1 = page_lines[i+1]
        if "abstract" in p1.text:
            track="abstract, full text not available"

        if "presentation" in p1.text:
            presentation = has_pdf(p1,1)
            presentation = urljoin(URL, presentation)

        try:
            pdf = has_pdf(p1)
            if pdf==None:
                continue
        except:
            continue        
        #print(p1)
        authors = namify(p1.text.split("–")[0])
       

        pdf = urljoin(URL, pdf)
        if pdf==URL:
            pdf=None
        try:    
            title = p.text
            title = title.split(":")[1]
        except:
            title = p.text
        title = unspace(title)
        title= remove_parenthesised(title)
        line = [title, authors, pdf, presentation, vol, track]
        writer.writerow(line)
