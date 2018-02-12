import pickle
from scipy.spatial import distance
import numpy

vfile="VirDkms.pickle"
pickle_in=open(vfile,"rb")
Vdict=pickle.load(pickle_in)
pickle_in.close()

dfile="BacDkms.pickle"
pickle_in=open(dfile,"rb")
Bdict=pickle.load(pickle_in)
pickle_in.close()

#now we have two nested dictionaries Vdict and Bdict
#we have the kmer counts for the {dict[key][k]:'counts\tcounts\t....' etc}

filename="NegsTrain11238ICC.tsv"
dist=[]
vKs=[]
bKs=[]
vK1=[]
bK1=[]
d1=[]
d2=[]
d3=[]
d4=[]
d5=[]
d6=[]
distE=[]
distBC=[]
distCrr=[]
distCB=[]
distCS=[]
distCos=[]
#distHam=[]
#d7=[]
#vKs1=[]
#bKs1=[]
ints=[]
#distMB=[]
#here choose vir-bac pair
#do smth for a variable kmer
#repeat the same for kmers[1:5]
with open(filename, 'r') as f:
    for line in f:
        line=line.rstrip()
        words=line.split('\t')
        vir=words[0] #string
        bac=words[1] #string
        ints.append(tuple([vir,bac])) #list of [tuples of (string,string)]
        #the above creates a tuple with the virus as ints[x][0]
        #and the bacteria as the ints[x][1]
        #similarly can create a tuple with virus-non host pairs
        for k in range(1,7):
            vK=Vdict[vir][k] #here we get a string , need to split and convert to float
            vK1=vK.split('\t')
            for x in vK1:
                vKs.append(float(x)) #list of all the 'k'mer counts for virus
            bK=Bdict[bac][k]
            bK1=bK.split('\t')
            for x in bK1:
                bKs.append(float(x)) #list of all the 'k'mer counts for bacteria
            # d1.append(float(distance.euclidean(vKs,bKs)))
            # d2.append(float(distance.braycurtis(vKs,bKs)))
            # d3.append(float(distance.correlation(vKs,bKs)))
            # d4.append(float(distance.cityblock(vKs,bKs)))
            # d5.append(float(distance.chebyshev(vKs,bKs)))
            # d6.append(float(distance.cosine(vKs,bKs)))
            d1.append(distance.euclidean(vKs,bKs))
            d2.append(distance.braycurtis(vKs,bKs))
            d3.append(distance.correlation(vKs,bKs))
            d4.append(distance.cityblock(vKs,bKs))
            d5.append(distance.chebyshev(vKs,bKs))
            d6.append(distance.cosine(vKs,bKs))
            #hamming distance is only useful if we make them boolean
            #d7.append(float(distance.hamming(vKs1,bKs1)))
            #Z = numpy.vstack([vKs,bKs])
            #A=numpy.cov(Z, rowvar=False)
            #B=inv(A)
            #d7.append(float(distance.mahalanobis(vKs,bKs,B)))
            bKs=[]
            vKs=[]
            #bKs1=[]
            #vKs1=[]
        nexd1 = '\t'.join(str(v) for v in d1)
        nexd2 = '\t'.join(str(v) for v in d2)
        nexd3 = '\t'.join(str(v) for v in d3)
        nexd4 = '\t'.join(str(v) for v in d4)
        nexd5 = '\t'.join(str(v) for v in d5)
        nexd6 = '\t'.join(str(v) for v in d6)
        #nexd7 = '\t'.join(str(v) for v in d7)
        d1=[]
        d2=[]
        d3=[]
        d4=[]
        d5=[]
        d6=[]
        #d7=[]
        distE.append(nexd1)
        distBC.append(nexd2)
        distCrr.append(nexd3)
        distCB.append(nexd4)
        distCS.append(nexd5)
        distCos.append(nexd6)
        #distHam.append(nexd7)

thefile = open('Train11238_E_dist.tsv', "w")
for item in distE:
    print>>thefile, item

thefile = open('Train11238_BC_dist.tsv', "w")
for item in distBC:
    print>>thefile, item

thefile = open('Train11238_Crr_dist.tsv', "w")
for item in distCrr:
    print>>thefile, item

thefile = open('Train11238_CB_dist.tsv', "w")
for item in distCB:
    print>>thefile, item

thefile = open('Train11238_CS_dist.tsv', "w")
for item in distCS:
    print>>thefile, item

thefile = open('Train11238_Cos_dist.tsv', "w")
for item in distCos:
    print>>thefile, item
