#!/bin/sh

for i in $(seq 1 3); do
    mkdir d$i
    find . -maxdepth 1 -name "*D$i*" -type f -exec mv {} "d$i" \;
done
