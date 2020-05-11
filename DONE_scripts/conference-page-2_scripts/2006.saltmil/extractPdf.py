import sys
sys.path.append('..')
from nameparser import HumanName
import os
authorList="""Mikel Forcada
Anna Sågvall Hein and Per Weijnitz
Stephen Krauwer
Christian Monson and Ariadna Font Llitjós and Roberto Aranovich and Lori Levin and Ralf Brown and Eric Peterson and Jaime Carbonell and Alon Lavie
Maja Popović and Hermann Ney
Delyth Prys
Daniel Yacob
Tod Allman and Stephen Beale
Saba Amsalu and Sisay Fissaha Adafre
Carme Armentano-Oller and Mikel Forcada
Arantza Casillas and Arantza Díaz de Illarraza and Jon Igartua and R. Martínez and Kepa Sarasola
Boštjan Dvořák and Petr Homola and Vladislav Kuboň
Adrià de Gispert and José B. Mariño
Jorge González and Antonio L. Lagarda and José R. Navarro and Laura Eliodoro and Adrià Giménez and Francisco Casacuberta and Joan M. de Val and Ferran Fabregat
Dafydd Jones and Andreas Eisele
Svetla Koeva and Svetlozara Lesseva and Maria Todorova
Mirjam Sepesy Mauèec and Zdravko Kaèiè
Sara Morrissey and Andy Way
Alicia Pérez and Inés Torres and Francisco Casacuberta and Víctor Guijarrubia
Kevin Scannell
Oliver Streiter and Mathias Stuflesser and Qiu Lan Weng
John Wogan and Brian Ó Raghallaigh and Áine Ní Bhriain and Eric Zoerner and Harald Berthelsen and Ailbhe Ní Chasaide and Christer Gobl
Pavel Zheltov
""".split('\n')

pagesList="""1
7
13
15
25
31
33
39
47
51
55
59
65
69
75
79
87
91
99
103
109
113
117
121
""".split("\n")
FULL_PDF='2006.saltmil.pdf'
SKIP_PAGE=6
def get_last_name(author):
    author = HumanName(author.split("and")[0])
    return author.last


def find_page(author_text,pageItem=0):
    author = get_last_name(author_text)
    cmd = "pdfgrep -p "+author+" ./"+FULL_PDF
    page = os.popen(cmd).read()
    pageOcc=page.split('\n')[pageItem]
    page = int(pageOcc.split(':')[0])

    return page

def make_pdf(pages,author,full_pdf,i=None):
    author=author.replace(" ","")
    cmd="qpdf "+full_pdf+" --pages "+full_pdf+" "+pages+" "+"-- paper-"+str(i)+"-"+author+".pdf"
    os.system(cmd)
    return None

i=0
for i in range(len(authorList)):

    authors = authorList[i]

    page = int(pagesList[i])+SKIP_PAGE
    page1 = int(pagesList[i+1])+SKIP_PAGE-1
    main_author = get_last_name(authors)
    pages = str(page)+'-'+str(page1)

    print("paper-"+str(i)+"-"+main_author+".pdf")
    make_pdf(pages, main_author, FULL_PDF, i)
