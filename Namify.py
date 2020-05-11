#!/usr/bin/env python3
"""
This script takes as an input a string containing a list of names and output the list of names with in the form "Last name, First name [Middle name]"


Example usage:

python Namify.py 'John B. Smith and Pablo Ramirez-Gonzalez and Bob Doe'
>>>Smith, John B. and Ramirez-Gonzalez, Pablo and Doe, Bob


Author: Marie Dubremetz
"""
from nameparser import HumanName
import sys
import re
from common import namify


if __name__ == "__main__":
    line=sys.argv[1]
    #namify(line)
    print(namify(line))