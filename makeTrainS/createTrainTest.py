
import random

filename="Negatives.tsv"
f1="Train"+filename
f2="Test"+filename

sTest=1100
fl=[]
ran=[]

ftr=[]
fte=[]

with open(filename, 'r') as f:
    for line in f:
        line=line.rstrip()
        fl.append(line)


#print len(fl)
# for i in range(1,1101):
#     ran.append(random.randint(0,11237))

ran=random.sample(range(0, len(fl)-1), sTest)

for x in range(1,len(fl)):

    if x in ran:
        fte.append(fl[x])
    else:
        ftr.append(fl[x])

print len(ftr)
print len(fte)


thefile = open(f1, "w")
for item in ftr:
    print>>thefile, item


thefile = open(f2, "w")
for item in fte:
    print>>thefile, item





filename="Positives.tsv"
f1="Train"+filename
f2="Test"+filename

sTest=1100
fl=[]
ran=[]

ftr=[]
fte=[]

with open(filename, 'r') as f:
    for line in f:
        line=line.rstrip()
        fl.append(line)


#print len(fl)
# for i in range(1,1101):
#     ran.append(random.randint(0,11237))

ran=random.sample(range(0, len(fl)-1), sTest)

for x in range(1,len(fl)):

    if x in ran:
        fte.append(fl[x])
    else:
        ftr.append(fl[x])

print len(ftr)
print len(fte)


thefile = open(f1, "w")
for item in ftr:
    print>>thefile, item


thefile = open(f2, "w")
for item in fte:
    print>>thefile, item
