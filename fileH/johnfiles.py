import glob, os, shutil, re

source_dir = '/hosts/linuxhome/mgx/tmp/PATRIC/20170614/'
dst = '/home/divyae/genomicData/PatData/'

file_list = list()

found = list()
tax_found = list()
files_found = list()

#notfound = list()
tax_notfound = list()

with open('/home/divyae/genomicData/PatData/ls_S_fna.txt', 'r') as myfile:
  for line in myfile:
    file_list.append(line.rstrip()) # = myfile.read().replace('\n', '')

with open("/home/divyae/genomicData/PatData/HostUnique_inPat.txt", 'r') as fread:
  for line in fread:
    taxonomy_id = line.rstrip()
    regex = '^'+ re.escape(taxonomy_id)+'\..+?\.fna$'
    
    matching_files = [x for x in file_list if re.match(regex,x)]
    if matching_files:
      #print taxonomy_id, "found!", str(len(matching_files))
      tax_found.append(taxonomy_id)
      found.append(len(matching_files))
      files_found.append(matching_files)
    else:
      #print taxonomy_id, "NOT found!"    
      tax_notfound.append(taxonomy_id)
      #notfound.append(str(len(matching_files))
    
file1 = open('/home/divyae/genomicData/PatData/tax_found.txt', 'w')
for item1 in tax_found:
  file1.write("%s\n" % item1)  
    
file2 = open('/home/divyae/genomicData/PatData/found.txt', 'w')
for item2 in found:
  file2.write("%s\n" % item2)  
  
file3 = open('/home/divyae/genomicData/PatData/files_found.txt', 'w')
for item3 in files_found:
  file3.write("%s\n" % item3)

file4 = open('/home/divyae/genomicData/PatData/tax_notfound.txt', 'w')
for item4 in tax_notfound:
  file4.write("%s\n" % item4)    

    
    
    
  
    #if re.match("r/^line\..+?\.fna$/",file_list):
    #if re.search(r'/^line \. .+? ',file_list):
      # file exists
    #found = re.search('r/^taxonomy_id\..+?\.fna$/',file_list)
    #search = re.search(r'/^line\..+?/',file_list)
    #search = re.search(r/^line\..+?/',file_list)
    #if found:
     # print found
   # else:
     # print "Not found"
      
          
      #sys.run("cp "+source_dir+search+" "+dst+filename)
    #else:
      # file does not exist
     #   print "you are screwed"
        
