#!/usr/bin/env python3.6
import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR performing pacakge upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely differerent string that alsoe has numbers [34567]")
print(result[1])

result = re.search(regex, "99 elephants in a [cage]")
print(result[1])

### Errors, check on 3.3.7