import math
import numpy
import scipy
import glob
import sys
import os.path
from scipy.spatial import distance


#filename = str(kmer) + "_mercount_relative.txt"

#files = []
#filename="4_mercount_relative.txt"
#files=glob.glob("*filename")



#[dist[:] for x in [[foo] * len(files)] * len(files)]  
#dist = [[[1 for i in range(6)] for j in range(6)] for k in range(7)]

dist = [[0 for i in range(6)] for j in range(6)]

#6 is the number of 


files = list ()

#disc = list ()

file10 = open("filelist_6.txt","r")
for k in file10:
	files.append(k.rstrip())
file10.close()


dirsize = int(len(files)) 
	
#print files


for i in range(0,dirsize):
    file1 = open(str(files[i]),"r")
    vector1 = []
    for x in file1:
	count = float(x.rstrip())
	vector1.append(count)
    file1.close()
		
    #print vector1
    for j in range(0,dirsize):
	#if i != j:
	vector2 = []
	file2 = open(str(files[j]),"r")		
	for y in file2:
	    count2 = float(y.rstrip())
	    vector2.append(count2)
	file2.close()
	#distance = dist_4mer(vector1, vector2,kmer)
	#distc = float(distance.euclidean(vector1,vector2))
	#disc.append(distc)	

	dist[i][j] = float(distance.euclidean(vector1,vector2))
	
	#print distance
	
    #print vector2

#print distance



print dist
