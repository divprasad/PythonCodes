#this script creates a pickle output file for
#the nested dictionary needed to make the tables

DB = {}
import pickle
import sys

fin=sys.argv[1]+"_bdict.tsv"
fout=sys.argv[1]+".pickle"

#with open("outB_27654921_106_bdict.tsv", "r") as f:
with open(fin, "r") as f:
    for line in f:
        line = line.rstrip()
        words = line.split()
        vir = words[0]
        bac = words[1]
        if vir not in DB:
            DB[vir] = {}
        if bac not in DB[vir]:
            DB[vir][bac] = {}


#pickle_out=open("DB_27654921_106.pickle","wb")
pickle_out=open(fout,"wb")
pickle.dump(DB,pickle_out)
pickle_out.close()
