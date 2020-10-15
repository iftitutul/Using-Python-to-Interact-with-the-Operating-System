#!/bin/bash

for file in ./bash-folder/*.py; do
   name=$(basename $file .py)
   # echo mv "$file" "$name.html" # check rename works or not
   mv "$file" "./bash-folder/$name.html"
done