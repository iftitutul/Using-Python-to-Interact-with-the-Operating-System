#!/usr/bin/env python3.6

def character_frequency(filename):
   """ Counts the frequency of each character inthe given file. """
   # First try to open the file
   try:
      f = open(filename)
   except OSError:
      return None
   
   # Now process the file
   characters = {}
   for line in f:
      for char in line:
         characters[char] = characters.get(char, 0) + 1
   f.close
   return characters

##  when writing a try-except block, the important thing to remember is that the code in the except block is only executed if one of the instructions in the try block raise an error of the matching type.
