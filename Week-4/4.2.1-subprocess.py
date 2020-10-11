#!/usr/bin/env python3.6

import subprocess

print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "2"]))

result = subprocess.run(["ls","this_file_doesn't_exist"])
print(result.returncode)

print(subprocess.run(["ping", "-c", "4", "google.com"]))
