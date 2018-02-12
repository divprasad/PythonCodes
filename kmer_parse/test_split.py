import os
from Bio import SeqIO


for seq_record in SeqIO.parse("mini27654921.fasta", "fasta"):

    #print seq_record.id
    #print seq_record.seq

    ##fname=seq_record.id.partition(">")[2]
    f1= open("tmpr", "w")
    print>>f1,">"+seq_record.id
    print>>f1, seq_record.seq
    f1.close()
