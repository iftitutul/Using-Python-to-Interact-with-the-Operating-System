#!/usr/bin/env python3.6

### Run the command: python3.6 4.1.3-data-cmd-argument.py <filename>

# Install sys module, Linux Command:  pip install os_sys
import sys
import os
print(sys.argv)

# The exit status is a value returned by a program to the shell. In all Unix-like operating systems, the exit status of the process is zero when the process succeeds and different than zero if it fails.

# Linux Command: wc 4.1.1-data-streams.py 
# Linux Command:  echo $? [Success, so returns 0]

# Linux Command: wc data-streams.py
# Linux Command:  echo $? [Fail, so returns 1]

filename = sys.argv[1]

if not os.path.exists(filename):
   with open(filename, "w") as f:
      f.write("New File created\n")
else:
   print("Error, the file {} alrady exists!".format(filename))
   sys.exit(0)


