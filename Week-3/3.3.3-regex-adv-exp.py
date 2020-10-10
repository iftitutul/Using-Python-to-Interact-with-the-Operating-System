#!/usr/bin/env python3.6
import re

def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  # result = re.search(r"^(\w*), (\w*.\w?\.?)$", name)
  if result is None:
    return name
  return("{} {}".format(result[2], result[1]))


name = rearrange_name("Kennedy, John F.")
print(name)
