import sys
try:
	stre = open('26200428.fasta', 'r');
	stre.seek(0);
	data = stre.readlines();
	stre.close();
except:
	print ("Unable to load file.")
	exit(1)
for line in data:
	if ">" in line:
		line = line.replace("-","_")

thefile = open('26200428Mod.fasta', "w")
for item in data:
    print>>thefile, item
	#sys.stdout.write(line)
