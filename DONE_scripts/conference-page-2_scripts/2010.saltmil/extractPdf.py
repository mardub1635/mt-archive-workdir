import sys
sys.path.append('..')
from nameparser import HumanName
import os
authorList="""Marc Kemps-Snijders
Antton Gurrutxaga and Igor Leturia and Eli Pociello and Iñaki San Vicente and Xabier Saralegi
Tommi A Pirinen and Krister Lindén
Aric Bills and Lori S. Levin and Lawrence D. Kaplan and Edna Agheak MacLean
Marco Passarotti
Anna Björk Nikulásdóttir and Matthew Whelpton
Gábor Prószéky and Attila Novák and István Endrédy and Beatrix Oszkó and László Fejes and Sándor Szeverényi and Zsuzsa Várnai and Beáta Wagner-Nagy
Géraldine Walther and Benoît Sagot
Hrafn Loftsson and Jökull Yngvason and Sigru´n Helgadóttir and Eiri̇́kur Rögnvaldsson
""".split('\n')

pagesList="""1
3
13
19
27
33
41
45
53
60
""".split("\n")
FULL_PDF='2010.saltmil.pdf'
SKIP_PAGE=4
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
