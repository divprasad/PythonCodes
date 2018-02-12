#!/home/divyae/PythonScripts

import itertools
import math
import glob

#for "k" mers
#pass k as a function argument

#making the kmer list #stackoverflow.com/questions/25942528/generating-all-dna-kmers-with-python
bases=['A','T','G','C']
#k = 4


for k in range (1, 7):



	kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]



	#reverse the sequence # via http://stackoverflow.com/questions/19570800/reverse-complement-dna
	revcompl = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])


	kmer_list = []

	for l in kmers:
	    rev = revcompl(l)
	    if l and rev not in kmer_list:
		kmer_list.append(l)



	#making a file of the list

	filename = str(k) + "_mers.txt"
	kmer_file = open(filename, "w")
	for i in kmer_list:
	    kmer_file.write(i + "\n")

	kmer_file.close()
