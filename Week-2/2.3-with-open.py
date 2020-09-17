#!/usr/bin/env python3

with open("sample.txt") as file:
   for line in file:
      print(line.upper())

with open("sample.txt") as text:
    for line in text:
	    print(line.strip())
