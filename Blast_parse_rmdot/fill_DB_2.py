
import pickle
import sys

fin=sys.argv[1]+".pickle"
fmid=sys.argv[1]+"_bdict.tsv"
fout=sys.argv[1]+"_table.pickle"

#pickle_in=open("DB_26200428_106.pickle","rb")
pickle_in=open(fin,"rb")
#pickle_in=open("DB_27654921.pickle","rb")
DB=pickle.load(pickle_in)
pickle_in.close()

newwords=[]
words=[]
exwords=[]
nexwords=[]

with open(fmid, "r") as f:
    for line1 in f:
        #del line1
        #del words[:]
        line1 = line1.strip()
        words = line1.split()
        vir = words[0]
        bac = words[1]
        bac = bac.split('.')[0]
        if not bool(DB[vir][bac]): #meaning that the Nested D for the particular Vir-Bac pair is empty.
            #so directly append line for this particular Vir-Bac pair
            del newwords[:]
            newwords.append(words[0])
            newwords.append(words[1])
            newwords.append(words[2])
            newwords.append(words[3])
            newwords.append(words[4])
            newwords.append(words[4]) #5
            newwords.append(words[5]) #6
            newwords.append(words[5]) #7
            newwords.append(words[6]) #8
            newwords.append(words[7]) #9 #bitscore_best
            newwords.append(float(words[7])/float(words[2])) #10 #best_bitscore/len(vir)
            newwords.append(words[7]) #11 #sum_bitscore
            newwords.append(float(words[7])/float(words[2])) #12 #sum of ( #bitscore/len(vir) )
            newline = '\t'.join(str(v) for v in newwords)
            DB[vir][bac]=newline

        if bool(DB[vir][bac]):
            del exwords[:]
            exline=DB[vir][bac]
            exwords=exline.split()
            del nexwords[:]
            nexwords.append(exwords[0])
            nexwords.append(exwords[1])
            nexwords.append(exwords[2])
            nexwords.append(exwords[3])
            nexwords.append(exwords[4])
            nexwords.append(float(exwords[5]) + float(words[4])) #5 sum_len
            nexwords.append(exwords[5]) #6
            nexwords.append(float(exwords[7]) + float(words[5])) #7 sum_score
            nexwords.append(exwords[8]) #8
            nexwords.append(exwords[9]) #9
            nexwords.append(exwords[10]) #10
            nexwords.append(float(exwords[11]) + float(words[7])) #11
            nexwords.append(float(exwords[12]) + float(words[7])/float(words[2])) #12
            nexline = '\t'.join(str(v) for v in nexwords)
            DB[vir][bac]=nexline

f.close()




pickle_out=open(fout,"wb")
pickle.dump(DB,pickle_out)
pickle_out.close()




#print DB.values()
#print DB['unknown_gi_551155515']['1104566.3']
#print DB['SUP05_AB_751_P07AB_905_26']['1194715.3']
