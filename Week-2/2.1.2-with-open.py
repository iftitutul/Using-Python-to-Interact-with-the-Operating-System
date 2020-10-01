#!/usr/bin/env python3
with open("sample.txt") as file:
   print(file.readline())

# When we use a "with" block, Python will automatically close the file
