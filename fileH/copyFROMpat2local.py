import re, os, shutil, sys
#directory you wish to copy all the files to.
#dst = "c:\path\to\dir"
#src = "c:\path\to\src\dir"
FList=sys.argv[1]

src = '/hosts/linuxhome/mgx/tmp/PATRIC/'
dst = '/home/divyae/divyae2/HOSTS/UniqueIdentifiers/FINALHOST_PHI/1julPATcopy/'

with open(FList, 'r') as fread:
    for line in fread:
        line=line.rstrip()
        lin1=line.split('/')[1]
        shutil.copyfile(src+line,dst+lin1)

#date;python ~divyae/SCRIPTS/fileH/copyFROMpat2local.py add.notVS.fna.host_SelcOff60.tsv > error.log;date;date
