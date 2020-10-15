#!/usr/bin/env python3.6

import sys
import subprocess

old_substring = "jane"
new_substring = "jdoe"

f = open(sys.argv[1], "r")
for line in f.readlines():
   old_name = line.strip()
   new_name = old_name.replace(old_substring,new_substring)
   subprocess.run(["mv", old_name, new_name])
f.close()

# Run Command:
# python3.6 6.4.0-qwiklab-changeJane.py ./data/oldfiles.txt
