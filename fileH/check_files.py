
import fileinput, os
stillneed = open("/home/divyae/metaData_ML/data_chen/csv/HostUnique_11.txt", "w")
for line in fileinput.input():
    for filename in [l.split('=')[1] for l in line.split() if l.find('out_fname=')!=-1]:
                        if not os.path.exists(filename):
        print >>stillneed, filename
