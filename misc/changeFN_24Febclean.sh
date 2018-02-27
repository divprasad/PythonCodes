#!/bin/bash

for name in mod_*
do
    newname="$(echo "$name" | cut -c5-)"
    mv "$name" "$newname"
done
