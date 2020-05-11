import os
numlist="""3	3
4	4
5	5
6	7
8	9
10	11
12	13
14	15
16	21
22	31
33	36""".replace('\t','-').split('\n')
print()
print(numlist)
PDF="1956.preconf.full.pdf"
for page in numlist:
  cmd="qpdf "+PDF+" --pages "+PDF+" "+page+" "+"-- 1956.preconf.p"+page+".pdf"
  print(cmd)
  os.system(cmd)