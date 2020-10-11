#

#!/usr/bin/env python3.6

import re

def show_ip(line):
  pattern = r"(IP \((\d+)\)$"
  result = re.search(pattern, line)
  return "{}".format.result[1]


print(show_ip("IP (192.16.0.1)"))
