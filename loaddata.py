#!/usr/bin/python

import sys

print "hello world"

fi = open("/home/kkirscht/Downloads/Mailing_CurrentSheet1_20170616.tsv","r")

for input in fi:
    record =  input.split('\t')

    for item in record:
        sys.write(item)

fi.close()