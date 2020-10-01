#!/usr/bin/env python3

import os
import datetime

os.remove("tt.txt")
os.rename("tt.txt","test.txt")

print(os.path.exists("sample.txt"))

#print(os.path.exists("tt.txt"))

print(os.path.getsize("sample.txt")) # Return file size in bytes

print(os.path.getmtime("sample.txt")) # Return Unix timestamp

# Use datetime module
timestamp = os.path.getmtime("sample.txt")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("sample.txt"))