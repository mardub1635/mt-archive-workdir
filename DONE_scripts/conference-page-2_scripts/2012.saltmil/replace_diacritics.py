diacritics="""´ı|í
a´|á
a¨|ä
A´|Á
u´|ú
o´|ó
e´|é
o¨|ö
Sˇ|Š"""
with open("2012.saltmil", "r") as f:
    text=f.read()
    for dia in diacritics.split('\n'):
        dia1=dia.split("|")[0]
        dia2=dia.split("|")[1]
        text=text.replace(dia1,dia2)
#print(text)
lines=text.split('\n')
titleText=""
for i in range(len(lines)):
    if (i%2) !=0:
        line=lines[i]+'"'
        titleText+=line
    else:
        line=lines[i]
        titleText+=line+"\n"      
print(titleText)