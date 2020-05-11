import sys
sys.path.append('..')
from nameparser import HumanName
import os
authorList="""Irena Bellert
Robert S. Betz and Walter Hoffman
C. G. Borkowski and L. R. Micklesen
Joyce M. Brady and William B. Estes
Elinor K. Charney
Jared L. Darlington
J. L. Dolby and H. L. Resnikoff
Ching-yi Dougherty
H. P. Edmundson
E. R. Gammon
Yves Gentilhomme
Vincent E. Giuliano
Kenneth E. Harper
David G. Hays
Lydia Hirschberg
Walter Hoffman and Amelia Janiotis and Sidney Simon
Joseph Jaffe
Ronald W. Jonas
Sheldon Klein
Edward S. Klima
Susumu Kuno
Sydney M. Lamb
W. P. Lehmann
D. Lieberman
L. R. Micklesen and P. H. Smith, Jr
A. Opler and R. Silverstone and Y. Saleh and M. Hildebran and I. Slutzky
Milos Pacak
E. D. Pendergraft
Warren J. Plath
Bertram Raphael
Robert Tabory
Wayne Tosh
John H. Wahlgren
Victor H. Yngve
Victor H. Yngve
""".split('\n')


def get_last_name(author):
    author = HumanName(author)
    return author.last


def find_page(author_text,pageItem=0):
    author = get_last_name(author_text)
    cmd = "pdfgrep -p "+author+" ./MT-1963-AMTCL.pdf"
    page = os.popen(cmd).read()
    pageOcc=page.split('\n')[pageItem]
    page = int(pageOcc.split(':')[0])

    return page

def make_pdf(pages,author,full_pdf,i=None):
    cmd="qpdf "+full_pdf+" --pages "+full_pdf+" "+pages+" "+"-- abstract-"+str(i)+"-"+author+".pdf"
    os.system(cmd)
    return None
i=0
triList=zip(authorList, authorList[1:], authorList[2:])
for authors0,authors,authors1 in triList:
    
    # authors0 = authorList[i-1]
    # authors = authorList[i]
    # authors1 = authorList[i+1]
    
    try:
        page0 = find_page(authors0)
        page = find_page(authors)
        page1= find_page(authors1)
    except:
        continue
    main_author=get_last_name(authors)
    if page0>page:
        page=find_page(authors,pageItem=1)
    if page1>page:
        pages=str(page)+'-'+str(page1)
    else:
        pages=str(page)+'-'+str(page)
    
    print("abract-"+str(i)+"-"+main_author+".pdf")
    make_pdf(pages,main_author,'MT-1963-AMTCL.pdf',i)
    i=i+1
    