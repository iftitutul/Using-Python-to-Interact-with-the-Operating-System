#!/usr/bin/env python3.6

# Run this command:  python3.6 4.3.4-filter-log.py syslog

import re
import sys

logfile = sys.argv[1]

usernames = {}

with open(logfile) as f:
   for line in f:
      if "CRON" not in line:
         continue
      pattern = r"USER \((\w+)\)$"
      result = re.search(pattern, line)
      if result is None:
         continue
      name = result[1]
      usernames[name] = usernames.get(name, 0) +1

print(usernames)
