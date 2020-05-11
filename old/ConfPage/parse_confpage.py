from urllib.request import urlopen
from bs4 import BeautifulSoup
import spacy
from spacy import displacy
from collections import Counter
import dateparser
import re
from urllib.parse import urlparse
f=open("confList1.csv",'w')
#Parse page
link="temp1"
#html = urlopen(link)
with open(link,'r') as g:
    html = g.read()
bs = BeautifulSoup(html, "html.parser")
pagelines = bs.find_all(['p'])
#NLP treatment
nlp = spacy.load("en_core_web_sm")

def getDate(doc):
    confTime={"year":"N/A","month":"N/A","day":"N/A"}
    for X in doc.ents:
        if X.label_=='DATE':
            try:
                ddata=dateparser.date.DateDataParser().get_date_data(X.text)
                dtype=ddata['period']
                dobj=ddata['date_obj']
                if dtype=="year":
                    dobj=ddata['date_obj']
                    confTime["year"]=dobj.year
                if dtype=="day" and dobj:
                    confTime["day"]=dobj.day
                    confTime["month"]=dobj.strftime("%b")
            except:
                pass
    return confTime

def getPlace(doc):
    place=""
    for tok in doc.ents:
        if tok.label_=='GPE':
            place+=tok.text+" "
    return place
import csv
def normaliseSpace(text):
    if type(text) is list:
        text=" ".join(text)

    text=re.sub('\s+'," ",text)
    text=text.strip()
    return text

def isTOC(a):
    a=a.lower()
    return "table" in a and "content" in a

def isPDF(a):
    toc=[ a for a in links if isTOC(a.getText())]
    if not toc:
        if a:
            return a[0]['href']
    else:
        return None

def formatDate(d):
    return "{}/{}/{}".format(d.setdefault("year", " "), d.setdefault("month", " "), d.setdefault("day", " "))

writer = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
log=csv.writer(open("log.csv","w"), delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["Conference Title", "Year","Month","Day","place","has TOC?","Link"])
#Look at each line <p> of html file
confName=""

for line in pagelines[5:]:
    #Check if there is a new conference name in bold
    boldText=[b.getText() for b in line.find_all(['b'])]
    currName=normaliseSpace(boldText)
    links=line.find_all(['a'])
    toc = [ a for a in links if isTOC(a.getText())]
    pdf=isPDF(links)
    tocURL=""
    hasTable="no"
    if toc:
        hasTable="yes"
        tocURL="http://www.mt-archive.info/"+urlparse(toc[0]['href']).path
    elif pdf:
        hasTable="no"
        tocURL="http://www.mt-archive.info/"+urlparse(pdf).path
    if currName:
        confName=currName

    doc=nlp(line.getText())
    confTime=getDate(doc)
    month=confTime["month"]
    day=confTime["day"]
    place=getPlace(doc)
    backupYear=re.findall("19\d\d|20|d\d",line.getText())
    if confTime['year']=="N/A":
        if backupYear:
            confTime['year']=backupYear
    writer.writerow([confName, confTime['year'],month,day,place,hasTable,tocURL])
