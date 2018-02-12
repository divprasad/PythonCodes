import sys

km_L=[]
words=[]

fout=sys.argv[1]+".tsv"

with open("FL.txt","r") as f1:
	for k in f1:
		del words[:]
		#del newl
		k = k.rstrip()
		words.append(k[:-4])

		with open(k,"r") as f2:
			for line in f2:
				line = line.rstrip()
				#wd = line.split('\t')
				wd = line.split(' ')
				words.append(wd[1])


		newl='\t'.join(str(v) for v in words)
		km_L.append(newl)


thefile = open(fout, "w")
for item in km_L:
    print>>thefile, item
