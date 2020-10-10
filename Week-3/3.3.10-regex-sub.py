#!/usr/bin/env python3.6
import re

result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(result)


result = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "lovelace, Ada")
print(result)