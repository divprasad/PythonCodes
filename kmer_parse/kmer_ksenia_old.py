#!/usr/bin/env python2
from itertools import tee, izip import random
#Function to reverse complement the DNA sequence and randomly choose the
#nucleotide for ambiguos letters
def revcompl(x):
    return ''.join([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'R' :
random.choice(['A', 'G']), 'Y' : random.choice(['C', 'T']), 'S' :
random.choice(['C', 'G']), 'W' : random.choice(['A', 'T']), 'K' :
random.choice(['T', 'G']), 'M' : random.choice(['A', 'C']), 'B' :
random.choice(['C', 'G', 'T']), 'D' : random.choice(['A', 'G', 'T']), 'H' :
random.choice(['A', 'C', 'T']), 'V' : random.choice(['A', 'G', 'C'])}[B] for B
in x][::-1])
#Sliding window function
def window(iterable, size):
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters)
#Main counting function
def counter2(seq, list_kmer):
    l = []
    for i in range(len(list_kmer)):
        l.append(0)
#Here you can specify what the range of k-mers you need. I used
#3-,4-,5-,6-,7-mers
    for kmer in range(3,8):
        for each in window(seq, kmer):
            km = ''.join(list(each))
            if km in list_kmer:
                l[list_kmer.index(km)] += 1
            else:
#Here you should check the complementarity of your kmer
                k = revcompl(km)
                if k in list_kmer:
                    l[list_kmer.index(k)] += 1
    return(l)
#I am building the whole list of kmers, i.e. all dimers, next trimers, 4-mers,
#5-mers, etc I am doing its copy to work with
list_kmer = mer_list[:]
#Launch the main function counter2 by providing it individual sequence as
#string, i.e. "TTTAAAACGA" and a copy of kmers
r = counter2(''.join(seqs), list_kmer)
