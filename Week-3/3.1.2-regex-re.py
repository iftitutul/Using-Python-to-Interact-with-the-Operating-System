#!/usr/bin/env python3.6

import re

log = "JULY 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
