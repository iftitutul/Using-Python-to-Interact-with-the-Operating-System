#!/usr/bin/env python3.6
import re

def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result is None:
    return name
  return("{} {}".format(result[2], result[1]))

print(rearrange_name("Loveace, Ada"))
print(rearrange_name("Rithie, Dennis"))
print(rearrange_name("Hopper, Grace M."))

### It's not work for Hopper, Grace M.