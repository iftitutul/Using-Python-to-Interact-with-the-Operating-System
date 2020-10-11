#!/usr/bin/env python3.6

# Run this command:  python3.6 4.3.1-filter-log-with-regex.py syslog

import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
   for line in f:
      if "CRON" not in line:
         continue
      pattern = r"USER \((\w+)\)$"
      result = re.search(pattern, line)
      print(result[1])

