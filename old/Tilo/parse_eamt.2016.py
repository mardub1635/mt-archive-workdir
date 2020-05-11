# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from bs4 import BeautifulSoup
import spacy
import csv
import re
from common import save_page,get_url,is_subtitle,has_pdf,namify,get_title

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
with open(FILE_NAME+".tsv", 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Authors", "Pdf", "Presentation",
                     "Volume_Name", "Raw_webtext"])

    for i in range(len(page_lines)-1):
        p = page_lines[i]
        p1 = page_lines[i+1]
        #get the track
        if is_subtitle(p):
            print("assigne", track)
            track = is_subtitle(p)
            writer.writerow([track])

            continue

        raw_text = p.get_text().replace("\n", " ")
        pdf = None
        #Skip presention line
        if has_pdf(p) and "presentation" not in p.text:
            pdf = has_pdf(p)
            print(pdf)

        presentation = None
        if "presentation" in p1.text:
            presentation = has_pdf(p1)

        if not pdf:

            continue
        l_1 = p1.get_text()
        authors = re.split("\d+", p1.get_text())[0]
        print(authors)
        authors = namify(authors)
        title = get_title(p)
        line = [title, authors, pdf, presentation, track, raw_text]
        writer.writerow(line)
