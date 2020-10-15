#!/bin/bash

>./data/oldfiles.txt

files=$(grep " jane " ./data/list.txt | cut -d' ' -f 3)
echo $files

for f in $files; do
  # if [ -e $HOME$f ]; then
    if [ -e $f ]; then
      #echo $HOME$f >> ./data/oldfiles.txt;
      echo $f >> ./data/oldfiles.txt;
   fi
done