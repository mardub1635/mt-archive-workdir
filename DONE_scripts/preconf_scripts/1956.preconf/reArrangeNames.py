# -*- coding: utf-8 -*-
"""

This script is an example of how to generate a tsv file from an mt-archive conference page.
NOTE: 
-Make sure the conferenceList.csv file is present in the parent folder
-The name of the script is important, make sure to have the code of the conference between a '_' and the '.py'
 extension for instance: parse_2002.amta.py
-Make sure the common.py file is present in the same or the parent folder.

Author: Marie Dubremetz

"""
import sys
sys.path.append('..')
from common import *


# save webpage
authors="""Erwin Reifler, Far Eastern Department, University of Washington, Seattle
A. Koutsoudas and R. Machol, Willow Run Laboratories, University of Michigan
L. E. Dostert, Institute of Languages and Linguistics, Georgetown University
Cambridge Language Research Unit, Cambridge, England
Gilbert W. King, International Telemeter Corp., Los Angeles, California
Kenneth E. Harper, Slavic Department, University of California, Los Angeles
† D. Panov, The Academy of Sciences, Moscow, U.S.S.R.
† Victor H. Yngve., Massachusetts Institute of Technology, Cambridge, Massachusetts
† A. Koutsoudas and R. Korfhage, Willow Run Laboratories, University of Michigan
† L. Brandwood, Birkbeck College Research Laboratory, University of London
"""
for author in authors.split('\n'):
    author=author.split(',')[0]
    author=author.replace('† ','')
    print(author)