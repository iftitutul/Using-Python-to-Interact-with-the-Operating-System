#!/bin/bash

echo "To view the contents of the file, use the following command:"
cat list.txt

echo "Catch all the "jane" lines:"
grep 'jane' list.txt 

echo "List only the files containing the string 'jane' and not include 'janez'."
grep ' jane ' list.txt

echo "Let's fetch the different fields by only numbers"
grep ' jane ' list.txt | cut -d' ' -f 1

echo "Let's fetch the different fields by name"
grep ' jane ' list.txt | cut -d' ' -f 2

echo "Let's fetch the different fields by filename"
grep ' jane ' list.txt | cut -d' ' -f 3

echo "Return a range of fields together by using:"
grep ' jane ' list.txt | cut -d' ' -f 1-3

echo "To return a set of fields together:"
grep ' jane ' list.txt | cut -d' ' -f 1,3

######## TEST COMMAND ###########

# check if a particular file is present in the file system. We do this by using the -e flag. This flag takes a filename as a parameter and returns True if the file exists.

echo "Check the existence of a file named jane_profile_07272018.doc using the following command:"
if test -e ~/data/jane_profile_07272018.doc; then
   echo "File exists"; 
else 
   echo "File doesn't exist"; 
fi

#######
echo "Create a file using a Redirection Operator"
> test.txt
echo "I am appending text to this test file" >> test.txt

#######
echo "Iteration"
for i in 1 2 3; do 
   echo $i; 
done

######

