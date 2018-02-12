bdict={}
import pickle

with open("parse_bac.tsv", "r") as pars:
    for pline in pars:
        pline=pline.rstrip()
        pwords=pline.split()
        bdict[pwords[0]]=pwords[1]
pars.close()

pickle_out=open("bdict.pickle","wb")
pickle.dump(bdict,pickle_out)
pickle_out.close()
