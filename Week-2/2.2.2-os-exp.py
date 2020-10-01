#!/usr/bin/env python3

import os

file = "tt.txt"
if os.path.isfile(file):
   print(os.path.isfile(file))
   print(os.path.getsize(file))
else:
   print(os.path.isfile(file))
   print("File not found")



