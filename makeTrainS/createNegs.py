
import random

filename="Train11238ICC.tsv"
fO="1Negs"+filename

ints=[]
nints=[]
bac1=[]
vir1=[]
vir2=[]

fbac="wodots_Bdict.txt"
fvir1="27654921_Vdict.txt"
fvir2="26200428_Vdict.txt"

#put the size of negative set here
lNeg=11238

with open(filename, 'r') as f:
    for line in f:
        line=line.rstrip()
        words=line.split('\t')
        vir=words[0] #string
        bac=words[1] #string
        ints.append(tuple([vir,bac]))

with open(fbac, 'r') as f:
    for line in f:
        line=line.strip()
        #print line
        bac1.append(line)

with open(fvir1, 'r') as f:
    for line in f:
        vir1.append(line.rstrip())

with open(fvir2, 'r') as f:
    for line in f:
        vir2.append(line.rstrip())


for x in range (1,lNeg+1):

    nbac=random.choice(bac1)
    if (random.uniform(0,1) <= 0.5):
        nvir=random.choice(vir1)
    else:
        nvir=random.choice(vir2)

    while [nvir,nbac] in ints:
        nbac=random.choice(bac)
        if (random.uniform(0,1) <= 0.5):
            nvir=random.choice(vir1)
        else:
            nvir=random.choice(vir2)
    nints.append(tuple([nvir,nbac]))

#print len(ints)
#print len(nints)

with open(fO, 'w') as fp:
    fp.write('\n'.join('%s' '\t' '%s' % x for x in nints))


    #do something to select
