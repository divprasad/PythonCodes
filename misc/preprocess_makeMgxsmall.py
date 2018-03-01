#!/usr/bin/env python
#a script that makes a single fasta file
#takes two arguments as input : (1) filename of the single file to be created
#and (2) the file extension of the vir or bac files

from Bio import SeqIO
import subprocess
import os, sys
import os.path
import pickle

file1=sys.argv[1]     #input file
file2=sys.argv[2]     #input file

vir={}
with open(file2, 'r') as f:
    for line in f:
        line=line.rstrip()
        line=str(line)
        vir[line]={}

my_file="miniMgx.fasta"


f1= open(my_file, "w")
for seq_record in SeqIO.parse(file1, "fasta"):    #iterates through all the sequences in each file
    if str(seq_record.id) in vir:
        print>>f1,">"+seq_record.id
        print>>f1, seq_record.seq
f1.close()
