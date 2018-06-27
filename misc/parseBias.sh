#!/bin/bash
#pass the file name  as $1 and kmer number as $2

perl GetNucFrequency_PerFile_varK.pl $1 $2 > OutFreq_PerFile.txt;
for x in $(seq 1 $3);
do perl Get-kmer-bias.pl OutFreq_PerFile.txt ${x}mer.txt > out_${x}.tsv;
done

for y in $(seq 1 $3);
do time perl GetNucFrequency_PerSeq_varK.pl ${y}Mod.fasta $2 > OutFreq_${y}_PerSeq.txt;
for x in $(seq 1 $3);
do perl Get-kmer-bias.pl OutFreq_${y}_PerSeq.txt  ${x}mer.txt >> out_${x}.tsv;
done;
done;

for x in 1 2 3 4 5 6;
do time perl GetNucFrequency_PerSeq_varK.pl ${x}Mod.fasta 6 > OutFreq_${x}_PerSeq.txt;
perl Get-kmer-bias.pl OutFreq_${x}_PerSeq.txt  ${x}mer.txt > out_${x}.tsv;
transpose out_${x}.tsv $'\t' > temp1; mv temp1 out_${x}.tsv;
done;
