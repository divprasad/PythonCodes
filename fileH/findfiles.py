import glob, os, shutil, re

source_dir = '/hosts/linuxhome/mgx/tmp/PATRIC/20170614/'
dst = '/home/divyae/genomicData/PatData/'

with open("/home/divyae/genomicData/PatData/HostUnique_inPat_test_path.txt", 'r') as fread:

    for line in fread:
        #print line
        files = glob.iglob(os.path.join(source_dir, line))
        files2 = glob.glob(os.path.join(source_dir, line))
        print files
        print files2
        #for name in glob.glob('/hosts/linuxhome/mgx/tmp/PATRIC/20170614/line*'):
            #print name

files = ['filename1', 'filename2', 'filename3']
print ('A %(files)s'% vars())

for filename in files:
    file1 = filename + "*" + "." + "txt"; print ('1 %(file1)s'% vars())
    file2 = ('%(file1)s') % vars (); print ('2 %(file2)s'% vars())
    file3=glob.glob(file2); print ('3 %(file3)s'% vars())

#for name in glob.glob('dir/*'):
#    print name


taxonomy_id = 13513
filename = "13513.4.something.fna"

for taxonomy_id in species_list:
  search = re.search("r/^taxonomy_id\..+?\.fna$/",file_list):
  if search.match():
    # file exists
    filename = search.match()
    sys.run("cp "+source_dir+filename+" "+dst+newname)
  else:
    # file does not exist

filename = "1251.4.fna"
