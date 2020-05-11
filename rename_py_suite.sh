#!/bin/bash
echo "toto"
result=${PWD##*/}
mv parse_*.py parse_$result.py
