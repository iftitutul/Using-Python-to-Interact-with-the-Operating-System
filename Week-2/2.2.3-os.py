#!/usr/bin/env python3

import os

print(os.getcwd())
os.mkdir("tt-new")

os.chdir("tt-new")
print(os.getcwd())

os.chdir("../")
os.rmdir("tt-new") # only works if directory is empty
print(os.getcwd())

print(os.listdir("."))

