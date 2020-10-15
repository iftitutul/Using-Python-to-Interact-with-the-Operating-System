#!/usr/bin/env python3.6

import sys

for line in sys.stdin:
   print(line.strip().capitalize())

## cat haiku.txt | python3.6 6.1.2-pipes.py
## or, 
## python3.6 6.1.2-pipes.py < haiku.txt

## cat haiku.txt  | tr ' ' '\n' | sort
## cat haiku.txt  | tr ' ' '\n' | sort | uniq -c | sort -nr | head
