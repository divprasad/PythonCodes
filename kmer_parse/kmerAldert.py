#!/usr/bin/env python
from collections import defaultdict
from itertools import chain, groupby
import os, sys
#import pandas as pd
import glob

def count_kmers(read, k):
    counts = defaultdict(list)
    num_kmers = len(read) - k + 1
    for i in range(num_kmers):
        kmer = read[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1
    return(counts)

for fasta_file in glob.glob('*.fasta'):
    basename = os.path.splitext(os.path.basename(fasta_file)) [0]
    with open(fasta_file) as f_fasta:
        for k, g in groupby(f_fasta, lambda x: x.startswith('>')):
            if k:
                sequence = next(g).strip('>\n')
            else:
                d1 = list(''.join(line.strip() for line in g))
                for item in d1:
                    item.upper()
                d2 = ''.join(d1)
                complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'U': 'N', 'M': 'N', 'R': 'N', 'W': 'N', 'S': 'N', 'Y': 'N', 'K': 'N', 'V': 'N', 'H': 'N', 'D': 'N', 'B': 'N', 'X': 'N'}
                reverse_complement = ''.join(complement.get(base, base) for base in reversed(d2))
                d3 = (d2+'NN'+reverse_complement)
                counting = count_kmers(d3, 5)
                for item in counting:
                    #output = basename, sequence, item, counting[item]
                    output = sequence, item, counting[item]
                    with open('kmer.out', 'a') as text_file:
                        #text_file.write("%s %s %s %s\n" % output)
                        text_file.write("%s %s %s\n" % output)
