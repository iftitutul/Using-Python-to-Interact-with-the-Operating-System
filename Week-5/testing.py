#!/usr/bin/env python3.6

import re

def rearrange_name(name):
   result = re.search(r"^([\w  .]*), ([\w .]*)$", name)
   if result is None: # fix for edge cases
     # return "" # fix for edge cases
     return name # fix for single_name test cases
   return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))

###From command line, for unit testing look like 
# python3.6
# from rearrange import rearrange_name
# rearrange_name("Lovelace, Ada")
