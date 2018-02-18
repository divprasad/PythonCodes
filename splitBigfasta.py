#!/usr/bin/env python
#a script that makes a single fasta file
#takes two arguments as input : (1) filename of the single file to be created
#and (2) the file extension of the vir or bac files

from Bio import SeqIO
import sys

file1=sys.argv[1]     #takes the filename of the single file to be created
k=sys.argv[2]
count=1
num=1
for seq_record in SeqIO.parse(file1, "fasta"):  #iterates through all the sequences in each file
    if count % int(k) == 0:
        num=num+1
    my_file="try_" +str(num)
    f1= open(my_file, "a")
    print>>f1,">"+seq_record.id
    print>>f1,seq_record.seq
    f1.close()
    count=count +1
