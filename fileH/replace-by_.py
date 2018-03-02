#!/usr/bin/env python

import sys


file1=sys.argv[1]     #input file
file2=sys.argv[2]  +"Mod.tsv"
try:
	stre = open(file1, 'r');
	stre.seek(0);
	data = stre.readlines();
	stre.close();
except:
	print ("Unable to load file.")
	exit(1)

for line in data:
	if ">" in line:
		line = line.replace("-","_")

thefile = open(file2, "w")
for item in data:
    print>>thefile, item
	#sys.stdout.write(line)
