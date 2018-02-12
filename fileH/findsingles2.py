
L=[]
import sys
try:
	stre = open('file_multiples_mod2.txt', 'r');
	stre.seek(0);
	data = stre.readlines();
	stre.close();
except:
	print ("Unable to load file.")
	exit(1)
for line in data:
    line=line.rstrip()
    L.append(line)



with open('ICCMod.tsv') as oldfile, open('ICCTrimMod.tsv', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in L):
            newfile.write(line)
