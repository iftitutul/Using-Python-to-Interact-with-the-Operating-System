#!/usr/bin/env python3.6

print("Don't mind me, just a bit of text here...")

# python3.6 6.1.1-redirect.py > output.txt

## Append the file
# python3.6 6.1.1-redirect.py >> output.txt

data = input("This will come from STDIN: ")
print ("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

## python3.6 6.1.1-redirect.py < output.txt

## python3.6 6.1.1-redirect.py < output.txt 2> error_file.txt

## 0 --- File Descriptor STDIN
## 1 --- File Descriptor STDOUT
## 2 --- File Descriptor STDERR

