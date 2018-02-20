#!/bin/python

# make a file with the headers of the kmers

import itertools
import math
import glob

#making the kmer list #stackoverflow.com/questions/25942528/generating-all-dna-kmers-with-python
bases=['A','C','G','T']

km = 6
kmer_list = []
newline=[]
FL="kmers.tsv"
kmer_file = open(FL, "w")
for x in range (1,km+1):
    kmers = [''.join(p) for p in itertools.product(bases, repeat=x)]
    revcompl = lambda y: ''.join([{'A':'T','G':'C','C':'G','T':'A'}[B] for B in y][::-1])
    #reverse the sequence # via http://stackoverflow.com/questions/19570800/reverse-complement-dna
    del kmer_list[:]
    for k in kmers:
        rev = revcompl(k)
        if k and rev not in kmer_list:
            kmer_list.append(k)
    newline='\t'.join(str(v) for v in kmer_list)
    print>>kmer_file, newline
    FL1=str(x)+"mer.tsv"
    kmer_line = open(FL1, "w")
    print>>kmer_line, newline
    kmer_line.close()
kmer_file.close()
