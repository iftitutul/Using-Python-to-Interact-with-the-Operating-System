#!/usr/bin/env python3.6

import os

## Linux command: env

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

## Linux Command: export FRUIT= Mango
