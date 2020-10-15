#!/usr/bin/env python3.6

import sys

for line in sys.stdin:
   words = line.strip().split()
   print(" ".join([word.capitalize() for word in words]))

# Run Command: 
# cat haiku.txt | python3.6 6.3.7-python.py 