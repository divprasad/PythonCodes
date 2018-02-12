import math
import numpy
import scipy
import glob

def dist_kmer(p1,p2,k):
    dist = 0
	if k == 1:
		r=2
	if k == 2:
		r=10
	if k == 3:
		r=32
	if k == 4:
		r=136
	if k == 5:
		r=512
	if k == 6:
		r=2080
	if k == 7:
		r=8192
	if k == 8:
		r=32896
    for i in range(r):
        dist += math.pow((p2[i] - p1[i]), 2)
    return math.sqrt(dist)

kmer=4

filename = str(kmer) + "_mercount_relative.txt"

files=glob.glob("*filename")

dirsize=len(files) + 1

for i in range (1,dirsize)
	file1 = open(files[i],"r")


vector1 = []
	    for i in file1:
		count = float(i.rstrip().split("\t")[1])
		vector1.append(count)
	    file1.close()


##

import math
import numpy
import scipy
import glob


def dist_kmer(p1,p2,k):
    dist = 0
	if k == 1:
		r=2
	if k == 2:
		r=10
	if k == 3:
		r=32
	if k == 4:
		r=136
	if k == 5:
		r=512
	if k == 6:
		r=2080
	if k == 7:
		r=8192
	if k == 8:
		r=32896
    for i in range(r):
        dist += math.pow((p2[i] - p1[i]), 2)
    return math.sqrt(dist)




filename = "4_mercount_relative.txt"
files=glob.glob("*4_mercount_relative.txt")
dirsize = len(files) + 1

for i in range (1,dirsize):
	file1 = open(files[i],"r")
		    vector1 = []
	    for i in file1:
		count = float(i.rstrip().split("\t")[1])
		vector1.append(count)
	    file1.close()
	for j in range (1, dirsize):
		if i!=j
			

