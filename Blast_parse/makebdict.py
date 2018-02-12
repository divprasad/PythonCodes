
bdict = {}
import pickle
#import sys

fin="help2.tsv"
fout="bdict.pickle"

with open(fin, "r") as f:
    for line in f:
        line = line.rstrip()
        words = line.split()
        bdict[words[0]]=words[1]
        #k = words[0]
        #v = words[1]
        #if v not in bdict:
        #    bdict[k] = {}
        #bdict[k]=v


pickle_out=open(fout,"wb")
pickle.dump(bdict,pickle_out)
pickle_out.close()
