from nameparser import HumanName
with open("tempName",'rb') as g:
    lines=g.readlines()
authorList=""
for line in lines:
    authors=HumanName(line)
    authorList += authors.last+", "+authors.first+" ; "
    print(authorList)