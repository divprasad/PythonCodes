#/bin/bash!

while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    sed -n -e "${line}p" 1stColumn >> DOAGAIN.txt
done < "$1"
