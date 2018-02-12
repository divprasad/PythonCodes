
#this script take the raw blast output file
#and then coverts the contig names of the bacteria to a species/ strain names

L=[]
import pickle
import sys

pickle_in=open("bdict.pickle","rb")
bdict=pickle.load(pickle_in)



fin=sys.argv[1]+".tsv"
fout=sys.argv[1]+"_bdict.tsv"

#with open("outB_26200428_405.tsv", "r") as fasta:
with open(fin, "r") as fasta:
    for fline in fasta:
        fline=fline.rstrip()
        fwords=fline.split()
        fwords[1]=bdict[fwords[1]]
        lin="\t".join(fwords)
        L.append(lin)

thefile = open(fout, "w")
for item in L:
    print>>thefile, item
