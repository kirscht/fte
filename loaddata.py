#!/usr/bin/python

print "hello world"

fi = open("/home/kkirscht/Downloads/Mailing_CurrentSheet1_20170616.tsv","r")

for input in fi:
    print input


fi.close()