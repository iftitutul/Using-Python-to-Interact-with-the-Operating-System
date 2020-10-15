#!/bin/bash

for i in $(cat haiku.txt); do 
   B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; 
   echo -n "${B}${i:1} "; 
done; 
echo -e "\n"

# Alternative 6.3.7-python.py