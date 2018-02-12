#!/bin/bash
#make kmer profile count for all files in a dir

#divyae@wildtype1:~/filefetch_patric/singles/18oct_kmer:cp *.fna ~divyae/filefetch_patric/singles/18oct_kmer/
#python make_kmerList.py

#ls *.fasta > FN_singles.txt #for viral contigs
ls *.fna > FN_singles.txt #for Bac genomes
python make_kmerList.py

date

 # mkdir 1mer
 # mkdir 2mer
 # mkdir 3mer
 # mkdir 4mer
 # mkdir 5mer
 # mkdir 6mer

for sequence (can be multiple lines) read from input fasta
print sequence to tmp fasta file

for i in {4..6}
do
  read first line of {$i}mer.tsv -> kmer_list and then close file
  print sequence_ID (append to ${i}mer.tsv)
  date
  suf="mer"
  suff="mers.txt"
  fl="$i$suf"
  fl1="${i}_$suff"
  mkdir $fl
  cp tabulate_kmer_woD.py ./$fl/
  cp ${fl1} ./$fl/
  while read line; do ~divyae/jellyfish-2.2.3/bin/jellyfish count -s 100000 -m $i -C $line; done < tmp fasta file
  # while read line; do ~divyae/jellyfish-2.2.3/bin/jellyfish count -s 100000 -m $i -C $line; done < tmp fasta file
  #while read line; do ~divyae/jellyfish-2.2.3/bin/jellyfish count -s 100000 -m $i -C -o ./$fl/${line%.fna}_mercount.jf $line; done < tmp fasta file
  #while read line; do ~divyae/jellyfish-2.2.3/bin/jellyfish count -s 100000 -m $i -C -o ./$fl/${line%.fasta}_mercount.jf $line; done < FN_singles.txt
  #line1="${line%.*}"; ~divyae/jellyfish-2.2.3/bin/jellyfish dump -c mer_counts.jf | sort &>> ./$fl/$line1.tsv; done < FN_singles.txt
  #line1="${line%.*}"; end="_$fl"; filename="$line1$end"; ~divyae/jellyfish-2.2.3/bin/jellyfish dump -c mer_counts.jf | sort &>> ./$fl/$filename.tsv; done < FN_singles.txt



  #cd $fl
  date

  ~divyae/jellyfish-2.2.3/bin/jellyfish mer_counts.jf >
  for x in *mercount.jf #pass indivdually as x - for all the files that end with "k"_mercount.jf

  while read
    do these_kmers=$(~divyae/jellyfish-2.2.3/bin/jellyfish dump $x $k | cut -f2- -d " ") #this ensures that any query that is not fetched is reported as 0
    do foreach kmer in kmer_list
    if (exists (these_kmers{kmer})) print "\t" these_kmers{kmer}
  else print "\t0"
    print "\n" (append)
    read k #i is the kmer in each line of the k_mer.txt file that we made above, and now query it againt the file that we passed as x
    do y=$(~divyae/jellyfish-2.2.3/bin/jellyfish query $x $k | cut -f2- -d " ") #this ensures that any query that is not fetched is reported as 0
    done < "$i"_mers.txt
    printf "${y}\n" >> {$i}mer.tsv #dump the desired output in this file
  done

  rm -f *mercount.jf


  # ls *.tsv > FL.txt
  # python tabulate_kmer_woD.py $fl
  # cd ..

done




# divyae@wildtype1:~/Kmeroutput/Vir/26200428:cp ~divyae/metaData_ML/contigsFasta_chen/mod/split_26200428/1mer/1mer.tsv .
# divyae@wildtype1:~/Kmeroutput/Vir/26200428:cp ~divyae/metaData_ML/contigsFasta_chen/mod/split_26200428/2mer/2mer.tsv .
