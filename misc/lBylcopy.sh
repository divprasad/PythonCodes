#/bin/bash!

while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    cp $line /home/divyae/divyae2/HOSTS/UniqueIdentifiers/26Feb_again
done < "$1"
