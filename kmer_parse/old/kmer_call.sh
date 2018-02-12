#!/bin/bash
#make kmer profile count for all files in a dir

#divyae@wildtype1:~/filefetch_patric/singles/18oct_kmer:cp *.fna ~divyae/filefetch_patric/singles/18oct_kmer/
#python make_kmerList.py

ls *.fasta > FN_singles.txt

date

 # mkdir 1mer
 # mkdir 2mer
 # mkdir 3mer
 # mkdir 4mer
 # mkdir 5mer
 # mkdir 6mer

for i in {4..5}
do
  date
  suf="mer"
  fl="$i$suf"
  mkdir $fl
  cp tabulate_kmer.py ./$fl/
  while read line; do ~divyae/jellyfish-2.2.3/bin/jellyfish count -s 100000 -m $i -C $line;
  line1="${line%.*}"; ~divyae/jellyfish-2.2.3/bin/jellyfish dump -c mer_counts.jf | sort &>> ./$fl/$line1.tsv; done < FN_singles.txt
  #line1="${line%.*}"; end="_$fl"; filename="$line1$end"; ~divyae/jellyfish-2.2.3/bin/jellyfish dump -c mer_counts.jf | sort &>> ./$fl/$filename.tsv; done < FN_singles.txt


  cd $fl
  date
  ls *.tsv > FL.txt
  python tabulate_kmer_woD.py $fl
  cd ..

done




# divyae@wildtype1:~/Kmeroutput/Vir/26200428:cp ~divyae/metaData_ML/contigsFasta_chen/mod/split_26200428/1mer/1mer.tsv .
# divyae@wildtype1:~/Kmeroutput/Vir/26200428:cp ~divyae/metaData_ML/contigsFasta_chen/mod/split_26200428/2mer/2mer.tsv .
