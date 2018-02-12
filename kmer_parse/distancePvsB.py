import math
import numpy
import scipy
import glob
import sys
import os.path
from scipy.spatial import distance
import subprocess


#next script should do this

#what do we need as inputs to this script?
#two ids -> the viral contig name and the bac
#grep the raw kmer counts





#this script should make dictionary with the




for k in range(1:7):

	#have one file that has combined the kmer outputs
	#open the folder for virs


	filename=str(k) + "_merTable.tsv"
	f1 = open(filelist,"r")
	for lin in f1:
		if 'viralcontig' in lin:
			lin=lin.rstrip()
			l1 = lin.split('\t', 1)[1]

			l2=l1.split('\t')
			l3 = l2 / np.linalg.norm(l2)

	#open the folder for bac

	filename=str(k) + "_merTable.tsv"
	f1 = open(filelist,"r")
	for lin in f1:
		if 'viralcontig' in lin:
			lin=lin.rstrip()
			v2 = lin.split('\t', 1)[1]




#print files


for i in range(0,dirsize):
    file1 = open(str(files[i]),"r")
    vector1 = []
    for x in file1:
	count = float(x.rstrip().split("\t")[1])
	vector1.append(count)
    file1.close()

    #print vector1
    for j in range(0,dirsize):
	#if i != j:
	vector2 = []
	file2 = open(str(files[j]),"r")
	for y in file2:
	    count2 = float(y.rstrip().split("\t")[1])
	    vector2.append(count2)
	file2.close()
	#distance = dist_4mer(vector1, vector2,kmer)
	#distance = dist_4mer(vector1, vector2,kmer)
	#distc = float(distance.euclidean(vector1,vector2))
	#disc.append(distc)

	dist[i][j] = float(distance.euclidean(vector1,vector2))
	#print distance

    #print vector2

#print distance
