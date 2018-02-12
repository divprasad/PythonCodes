

L=[]

with open("Bac.tsv", 'r') as f:
    for line in f:
        line=line.rstrip()
        line1=line
        if "." in line1:
            line1=line1.split(".")[0]

        L.append(line1)

thefile = open("BacMod.tsv", "w")
for item in L:
    print>>thefile, item
