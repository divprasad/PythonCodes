import pickle
import numpy
import matplotlib.pyplot as plt
import sys

fin=sys.argv[1]+".pickle"
fout=sys.argv[1]+"_hist.png"
fmid="V_"+sys.argv[1]+"_uniq.tsv"

#pickle_in=open("DB_26200428_106.pickle","rb")
pickle_in=open(fin,"rb")
#pickle_in=open("DB_27654921.pickle","rb")
DB=pickle.load(pickle_in)

D=[]

#with open("V_outB_26200428_106_uniq.tsv", "r") as f1:
#with open("V_outB_27654921_uniq.tsv", "r") as f1:

#this makes a list of Unique_viruses from the blast output
#now we can append this to a list
#and use that list as an argument for fetching the length (number) of
#bacterial hits in the  blasts


with open(fmid, "r") as f1:
    for line1 in f1:
        line1=line1.rstrip()
        D.append(line1)
f1.close()

#so the list length will give us the distrubution of number of bac hits for all
#viruses in a seq manner

length=[]
for i in xrange(len(D)):
    length.append(len(DB[D[i]]))

#print length
#bins=numpy.linspace(0,200,200)

#plt.scatter(xrange(len(length)), length)
#plt.savefig('27654921_sc.png',dpi=150)
#plt.plot(length)
#plt.savefig('27654921_pl.png',dpi=150)
#plt.hist(length,bins)
#plt.savefig('27654921_hist.png',dpi=150)
#plt.savefig(fout,dpi=150)
