cat bigFasta.fna | grep "^>" > BacHeaders.txt
#cut -f1,22 -d " " BacHeaders.txt > help.tsv
awk -F ' ' '{print $1, $NF}' BacHeaders.txt > help.tsv
rev help.tsv | cut -c2- | rev | cut -c2- > help2.tsv
cut -d " " -f1 help2.tsv > help3.tsv
cut -d " " -f2 help2.tsv > help4.tsv
paste -d "\t" help3.tsv help4.tsv > help5.tsv

python makebdict.py
