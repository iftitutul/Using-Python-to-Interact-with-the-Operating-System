#!/usr/bin/env python3.6

import re

print(re.search(r".com","welcome"))

print(re.search(r"\.com", "welcome"))

print(re.search(r"\.com", "www.example.com"))

print(re.search(r"\w*", "This is an example"))

print(re.search(r"\w*","And_this_is_matter"))

