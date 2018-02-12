import glob
import shutil

SOURCE_PATH = '/hosts/linuxhome/mgx/tmp/PATRIC/20170614'
DEST_PATH = '/home/divyae/genomicData/PatData/'


dest_dir = "C:/test"
for file in glob.glob(r'C:/*.txt'):
    print file                                                                                                                                        
    shutil.copy(file, dest_dir)