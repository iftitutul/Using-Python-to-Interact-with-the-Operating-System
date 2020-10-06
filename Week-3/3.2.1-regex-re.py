#!/usr/bin/env python3.6

import re

result = re.search(r"aza", "plaza")
print (result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x","xeron"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "clapping"))

print(re.search(r"p.ng", "sponge"))

print(re.search(r"t.on$", "python"))

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
