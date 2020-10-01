#!/usr/bin/env python3.6

file = open("sample.txt")
print(f'file readline: {file.readline()}')

print(f'file 2nd readline: {file.readline()}')

print(f'file read: {file.read()}')

file.close()