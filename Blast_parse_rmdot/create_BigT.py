
import pickle
import sys
import subprocess



lin1=[]

fin=sys.argv[1]+"_table.pickle" 	 # stores the nested D in binary o/p format
fmid=sys.argv[1]+"_bdict.tsv"      	 # converted bact contigs to specices
fout=sys.argv[1]+"_parseOP_recurse.tsv"
fout1=sys.argv[1]+"_parseOP_bdict.tsv"
fout2=sys.argv[1]+"_parseOP_iteritems.tsv"

#fin="outB_26200428_405"+"_table.pickle"
pickle_in=open(fin,"rb")
#pickle_in=open("DB_27654921.pickle","rb")
DB=pickle.load(pickle_in)
pickle_in.close()


def recurse(d):
  if type(d)==type({}):
    for k in d:
      recurse(d[k])
  else:
      lin1.append(d)

recurse(DB)
#subprocess.call("cd results")
thefile = open(fout, "w")
for item in lin1:
    print>>thefile, item




# del lin1[:]
# with open(fmid, "r") as f:
#     for line in f:
#         line = line.rstrip()
#         words = line.split()
#         vir = words[0]
#         bac = words[1]
#         lin1.append(DB[vir][bac])
# thefile1 = open(fout1, "w")
# for item in lin1:
#     print>>thefile1, item
#
#
#
# del lin1[:]
# for i in DB.keys():
#     for j in DB[i][j].keys():
#         lin1.append(j)
#
# thefile2 = open(fout2, "w")
# for item in lin1:
#     print>>thefile2, item
