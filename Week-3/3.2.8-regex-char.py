#!/usr/bin/env python3.6

import re

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+","golfish"))

print(re.search(r"o+l+","hollywood"))

print(re.search(r"0+l+","boil"))


print(re.search(r"p?each","to each their own"))
print(re.search(r"p?each", "I like peaches"))
