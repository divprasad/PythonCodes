from subprocess import call

#subprocess.call("ls > FN_singles.txt")
FL=call(["ls"])
make_kmerList.py

kmer_list=[]
bases=['A','T','G','C']

# with open("1mer.txt","r") as f1:
#     for line in f1:
#         line=line.rstrip()
#         kmer_list.append(line)

#do for a single file first dumb fuck
for k in range (1, 7):

    	kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]
    	#reverse the sequence # via http://stackoverflow.com/questions/19570800/reverse-complement-dna
    	revcompl = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])

    	for l in kmers:
    	    rev = revcompl(l)
    	    if l and rev not in kmer_list:
    		kmer_list.append(l)


        ~divyae/jellyfish-2.2.3/bin/jellyfish count -s 100000 -m $i -C $line

        "~divyae/jellyfish-2.2.3/bin/jellyfish dump -c -t mer_counts.jf"
