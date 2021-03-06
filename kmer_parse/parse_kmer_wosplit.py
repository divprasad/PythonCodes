import subprocess
import os
import itertools
import math
import glob


kmer_list=[]
kmword=[]
kmline=[]
l2=[]
bases=['A','C','G','T']

#global out

kmers_found={}


def runJF (f1,k):
    #subprocess.call(['~divyae/jellyfish-2.2.3/bin/jellyfish count -C -s 100000 -m', 'k1','Actinobacteria_gi_319434515.fasta'])
    subprocess.call("~divyae/jellyfish-2.2.3/bin/jellyfish count -C -s 100000 -m '%s' '%s'" % (k, f1), shell = True)
    p=subprocess.Popen("~divyae/jellyfish-2.2.3/bin/jellyfish dump -c -t mer_counts.jf", shell=True, stdout=subprocess.PIPE)
    out=p.stdout.read().rstrip().split('\n')
    return out

def getkms(k):
    del kmer_list[:]
    kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]
    #reverse the sequence # via http://stackoverflow.com/questions/19570800/reverse-complement-dna
    #revcompl = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
    revcompl = lambda x: ''.join([{'A':'T','G':'C','C':'G','T':'A'}[B] for B in x][::-1])
    for l in kmers:
      rev = revcompl(l)
      if l and rev not in kmer_list:
        kmer_list.append(l)



m=subprocess.Popen("ls *.fasta", shell=True, stdout=subprocess.PIPE)
FL=m.stdout.read().rstrip().split('\n')

#print FL

#revcompl1 = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])

for i in range(1,7):

  subprocess.call("date", shell =True)
  getkms(i)
  fout=str(i)+"_merTable.tsv"
  del kmline[:]
  del l2[:]

  #l2.append("#contig_id")
  #for l in kmer_list:
#    l2.append(l)
  #kmline.append('\t'.join(str(v) for v in l2))

  for file1 in FL:
    del kmword[:]
    out1=runJF(file1,i)
    fname=file1.split('.f')[0]

    for line in out1:
      line = line.rstrip()
      words = line.split('\t')
      kmers_found[words[0]]=words[1]

    for l in kmer_list:
        if l not in kmers_found:
            kmers_found[l] = 0

    kmword.append(fname)
    for l in kmer_list:
        kmword.append(kmers_found[l])
    kmline.append('\t'.join(str(v) for v in kmword))

  thefile = open(fout, "w")
  for item in kmline:
    print>>thefile, item
