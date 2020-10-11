#!/usr/bin/env python3.7

# Heads up! This example uses the capture_output parameter of subprocess.run, which was introduced in Python 3.7. Please make sure you are running Python 3.7 or later to follow along.

import subprocess

result = subprocess.run(["host", "8.8.8.8"],capture_output=True)
print(result.returncode)
print(result.stdout)

# Output :
# 0
# b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'

# B tells us that this string is not a proper string for Python. It's actually an array of bytes. An array of bytes, this is a complex subject so listen closely. Data in computers is stored and transmitted in bytes and each can represent up to 256 characters. If we want this to become a proper string, we can call the decode method.
# Nowadays, most people use UTF-8 encoding, which is part of the Unicode standard that lists all the possible characters that can be represented.

print(result.stdout.decode().split())

### Another Example for stderr

result = subprocess.run(["rm","doesn't_exist"], capture_output = True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
