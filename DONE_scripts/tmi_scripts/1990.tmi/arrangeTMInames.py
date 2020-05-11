import sys
sys.path.append('..')
from common import namify, unspace

with open("names","r") as f:
    names=f.readlines()
    for name in names:
        name=namify(name)
        print(name)