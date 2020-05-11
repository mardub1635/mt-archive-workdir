import sys
sys.path.append('..')
from nameparser import HumanName
import os
authorList="""Lars Borin
Adam Ussishkin and Jerid Francom and Dainon Woudstra
Seid Muhie Yimam and Mulugeta Libsie
Izaskun Fernandez and Iñaki Alegria and Nerea Ezeiza
Juan A. Pereira Varela and Silvia Sanz-Santamaría and Julián Gutiérrez Serrano
David Chan and Dewi Jones and Oggy East
Gruffudd Prys
Llio Humphreys
Florie Moulin and Laura Laluque and Geróid Ó Néill
""".split('\n')

pagesList="""1
9
17
27
45
51
55
63
73
81""".split("\n")
FULL_PDF='2009.saltmil.pdf'
SKIP_PAGE=10
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
    print(pagesList[i])
    page = int(pagesList[i])+SKIP_PAGE
    page1 = int(pagesList[i+1])+SKIP_PAGE-1
    main_author = get_last_name(authors)
    pages = str(page)+'-'+str(page1)

    print("paper-"+str(i)+"-"+main_author+".pdf")
    make_pdf(pages, main_author, FULL_PDF, i)
