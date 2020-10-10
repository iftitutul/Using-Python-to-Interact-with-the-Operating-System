#!/usr/bin/env python3.6
import re

result = re.split(r"[.?!]", "One Sentence. Another one? And the last one!")
print(result)

result = re.split(r"([.?!])", "One Sentence. Another one? And the last one!")
print(result)

result = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(result)
