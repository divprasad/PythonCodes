import pickle
import subprocess

#after running parse_kmer_wsplit.py and running a bunch of lines in bash
#a small script in R

#do this : create a nested dictionary with the Bac/Vir as the first key
# and the kmer number as the second key

#so this create a pickle output file can we can load in the next function
#that will make any sort of comparisions/ correlations betweeen the

Vdict={}

subprocess.call("date", shell =True)
for k in range(1,7):
#have one file that has combined the kmer outputs
#open the folder for virs
#/home/divyae/Kmeroutput/Bac/Bfrac/FinalBackmers
    filename=str(k) + "_merTfrac_vir.tsv"
    with open(filename, 'r') as f:
        for line in f:
            line=line.rstrip()
            val =line.split('\t', 1)[1]
            key1=line.split('\t', 1)[0]
            if key1 not in Vdict:
                Vdict[key1]={}
            if k not in Vdict[key1]:
                Vdict[key1][k]={}

            Vdict[key1][k]=val


#print Vdict['Actinobacteria_gi_257461662'][2]



fout="VirD.pickle"

pickle_out=open(fout,"wb")
pickle.dump(Vdict,pickle_out)
pickle_out.close()
subprocess.call("date", shell =True)
