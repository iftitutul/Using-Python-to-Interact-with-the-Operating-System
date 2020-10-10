#!/usr/bin/env python3.6
import re

print(re.search(r"[a-zA-z]{5}", "a ghost"))

print(re.search(r"[a-zA-z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-z]{5}", "a scary ghost appeared"))

print(re.findall(r"\b[a-zA-z]{5}\b", "a scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))

print(re.search(r"s\w{,20}", "I really like strawberries"))
