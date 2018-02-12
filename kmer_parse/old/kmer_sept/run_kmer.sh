#!/bin/bash

#date
#make k-mer list for the k-mer from {1:desiered length} 
python make_kmerList.py

#date
#run the jellyfish program for all the fasta files in the folder
for ((k=1; k<=6; k++)) 
do for i in *.fasta; do ~divyae/jellyfish/jellyfish-2.2.3/bin/jellyfish count -m $k -s 100000 -t 24 -C -o ${i%.fasta}_${k}_mercount.jf $i; done #closing loop for the fasta files
done

#date


#./kmer_list.sh

for ((k=1; k<=6; k++)) 
do for x in *${k}_mercount.jf #pass indivdually as x - for all the files that end with "k"_mercount.jf
do while read i #i is the kmer in each line of the k_mer.txt file that we made above, and now query it againt the file that we passed as x  
do y=$(~divyae/jellyfish/jellyfish-2.2.3/bin/jellyfish query $x $i | cut -f2- -d " ") #this ensures that any query that is not fetched is reported as 0
printf "${i} \t ${y} \n" >> ${x%jf}txt #dump the desired output in 
done < "$k"_mers.txt
done
#date
done

#date




####DISTANCES GENE to GENOME RELATIVE
#FIRST MAKING RELATIVE KMER COUNTS
#make it relative genome
for a in *mercount.txt; do awk 'BEGIN { sum = 0 } { sum += $2 } END { print sum }' $a | while read i; do awk -v i=$i '{ printf "%s\t%s\n", $1, $2/i}' $a; done > ${a%.txt}_relative.txt; done

mkdir relative

cp *_relative.txt ./relative/

cd relative



#now calculate the 



ls | grep "*6_mercount_relative.txt" > filelist_6.txt

python RelDist.py
