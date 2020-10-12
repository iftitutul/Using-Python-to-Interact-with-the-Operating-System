#!/usr/bin/env python3.6

def validate_user(username, minlen):
   assert type(username) == str, "username must be a string"
   if minlen < 1:
      raise ValueError("minlen must be at least 1")
   if len(username) < minlen:
      return False
   if not username.isalnum():
      return False
   return True


""" print(validate_user("", 1))
print(validate_user("myuser", 1))
print(validate_user([], 1))
print(validate_user(["name"], 1))
print(validate_user("", -1))
print(validate_user(88,1))
print(validate_user([3], 1)) """

# we should use raise to check for conditions that we expect to happen during normal execution of our code and assert to verify situations that aren't expected but that might cause our code to misbehave
