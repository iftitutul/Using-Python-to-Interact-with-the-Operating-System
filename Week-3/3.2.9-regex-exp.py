#!/usr/bin/env python3.6

import re

print(re.search(r"A.*a","Argentina"))

print(re.search(r"A.*a", "Ajarbaijan"))

print(re.search(r"^A.*a$", "Ajarbaijan"))

print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-z_][a-z0-9_]*$"
print(re.search(pattern,"_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isnt a valid variable name"))
print(re.search(pattern, "my_varirable1"))
print(re.search(pattern, "99_variable_name"))
