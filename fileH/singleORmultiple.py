#!/bin/env python2

import sys
from Bio import SeqIO

fasta_file=sys.argv[1]
sep=sys.argv[2]

print sep
singleF="singles."+fasta_file
multipleF="multiples."+fasta_file

oneF = open(singleF, "w")
mulF = open(multipleF, "w")

for seq_record in SeqIO.parse(fasta_file, "fasta"):
	if sep in seq_record.id:
		print>>mulF, ">" + seq_record.id
		print>>mulF, seq_record.seq
	else:
		print>>oneF, ">" + seq_record.id
        print>>oneF, seq_record.seq

oneF.close()
mulF.close()
