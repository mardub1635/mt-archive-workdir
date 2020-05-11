import sys
sys.path.append('..')
from nameparser import HumanName
import os
authorList="""Elaine Uí Dhonnchadha and Alessio Frenda and Brian Vaughan
Wondwossen Mulugeta and Michael Gasser
Kristín Bjarnadottir
Fadoua Ataa Allah and Siham Boulaknadel
Tommi A. Pirinen and Francis M. Tyers
Borbála Siklósi and György Orosz and Attila Novák and Gábor Prószéky
Linda Wiechetek
Michael Gasser
Paola Carrion Gonzalez and Emmanuel Cartier
Denys Duchier and Brunelle Magnana Ekoukou and Yannick Parmentier and Simon Petitjean and Emannuel Schang
Tjerk Hagemeijer and Iris Hendrickx and Abigail Tiny and Haldane Amaro
Sigrún Helgadóttir and Á sta Svavarsdóttir and Eiríkur Rögnvaldsson and Kristín Bjarnadóttir and Hrafn Loftsson
Laurette Pretorius and Sonja Bosch
Björn Gambäck
Guy De Pauw and Gilles-Maurice de Schryver and Janneke van de Loo
Gulshan Dovudov and Vít Suchomel and Pavel Šmerk
""".split('\n')

pagesList="""1
7
13
19
25
29
35
41
47
55
61
67
73
79
85
93
99
""".split("\n")
FULL_PDF='2012.saltmil.pdf'
SKIP_PAGE=8
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

    print("paper-"+str(i+1)+"-"+main_author+".pdf")
    make_pdf(pages, main_author, FULL_PDF, i+1)
