#!/usr/bin/python

import sys

fi = open("/home/kkirscht/Downloads/Mailing_CurrentSheet1_20170616.tsv","r")

for input in fi.rstrip():
    record =  input.split('\t')

    for item in record:
        sys.stdout.write(item)
fi.close()