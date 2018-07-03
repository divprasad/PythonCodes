#!/usr/bin/env python2
import sys

sel=sys.argv[1]
pat=sys.argv[2]

FL={}
fullP=[]

with open(pat, 'r') as myfile:
    for line in myfile:
        line=line.rstrip()
        lin1=line.split('/')[1]
        if line not in FL:
            FL[lin1] = {}
            FL[lin1]=line


with open(sel, 'r') as myF:
    for line in myF:
        line=line.rstrip()
        if line in FL:
            fullP.append(FL[line])
        else:
            fullP.append("NOTFOUND")


f1= open("add."+sel, "w")
for k in fullP:
	    print>>f1, k
f1.close()
