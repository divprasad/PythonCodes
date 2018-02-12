import re, os, shutil
#directory you wish to copy all the files to.
#dst = "c:\path\to\dir"
#src = "c:\path\to\src\dir"

src = '/hosts/linuxhome/mgx/tmp/PATRIC/20170614'
dst = '/home/divyae/genomicData/PatData/'

#SOURCE_PATH = '/hosts/linuxhome/mgx/tmp/PATRIC/20170614'
#DEST_PATH = '/home/divyae/genomicData/PatData/'



with open("/home/divyae/genomicData/PatData/HostUnique_inPat_test.txt", 'r') as fread:

    for line in fread:
        match = re.search(r'Include',line)
        if match:
            loc = line.split('"')
            #concatenates destination and source path with subdirectory path and copies file over.
            dst_file_path = "%s\%s" % (dst,loc[1])
            (root,file_name) = os.path.splitext(dst_file_path)


            # Creates directory if one doesn't exist

            #if not os.path.isdir(root):
            #         os.makedirs(root)

            #src_file_path = os.path.normcase("%s/%s" % (src,loc[1]))
            #shutil.copyfile(src_file_path,dst_file_path)
            #print dst + loc[1]