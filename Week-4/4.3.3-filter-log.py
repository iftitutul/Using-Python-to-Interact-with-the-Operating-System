#!/usr/bin/env python3.6

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)

usernames[name] = usernames.get(name, 0) + 1
print(usernames)
