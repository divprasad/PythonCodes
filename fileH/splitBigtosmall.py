from Bio import SeqIO
import sys

file1=sys.argv[1]     #takes the filename of the single file to be created
for seq_record in SeqIO.parse(file1, "fasta"):  #iterates through all the sequences in each file
    name=(seq_record.id).split('/')[0]
    my_file=name + ".fasta"
    f1= open(my_file, "w")
    print>>f1,">"+seq_record.id
    print>>f1,seq_record.seq
    f1.close()
