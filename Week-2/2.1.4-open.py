#!/usr/bin/env python3

file = open("sample.txt")
lines = file.readlines()
file.close()

lines.sort()
print(lines)
