#!/usr/bin/env python


import subprocess
import os, sys
import pickle


file1=sys.argv[1]     #input file
#file2=sys.argv[2]+".pickle"
file3=sys.argv[2]
VC={}
out=[]
with open(file1, 'r') as f:
    for line in f:
        line=line.rstrip()
        words =line.split('\t')

        if "EV_" in words[0]:
            words[0]=words[0].split('EV_')[1]
        if "GOV_" in words[0]:
            words[0]=words[0].split('OV_')[1]
        if "irS_" in words[0]:
            words[0]=words[0].split('irS_')[1]
        if "|_" in words[0]:
            words[0]=words[0].split('|_')[1]

        for x in words:
            if "EV_" in x:
                x=x.split('EV_')[1]
            if "GOV_" in x:
                x=x.split('OV_')[1]
            if "irS_" in x:
                x=x.split('irS_')[1]
            if "|_" in x:
                x=x.split('|_')[1]
            VC[x]={}
            VC[x]=words[0]
        # if len(words) == 1:
        #     VC[words[0]]={}
        #     VC[words[0]]=words[0]
        # else:
        #     for x in words:
        #         VC[x]={}
        #         VC[x]=words[0]
        #     #VC[line]={}

with open(file3, 'r') as f:
    for line in f:
        try:
            out.append(VC[line])
        except :
            out.append(line)

thefile = open('totalVir_VC.out', "w")
for item in out:
    print>>thefile, item
thefile.close()
