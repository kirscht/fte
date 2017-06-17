#!/usr/bin/python

import sys

fi = open("/home/kkirscht/Downloads/Mailing_CurrentSheet1_20170616.tsv","r")

for input in fi:
    record =  input.rstrip().split('\t')

    address = record[0].split(' ')

    sys.stdout.write("%s\t" % address[0])
    sys.stdout.write("%s\t" % ' '.join(address[1:]))
    sys.stdout.write("%s\n" % '\t'.join(address[2:]))

#    for item in record:
#        sys.stdout.write("%s\t" % item)

#    sys.stdout.write('\n')
fi.close()

#ShortPropertyAddressZipcodeToNameAddresseeStreetCityStateZip
#151 Canyoncrest07052-4565GhanshyamGhanshyam & Pushpa Lalla4 Oconnor CirWest Orange, NJ 07052-4565
