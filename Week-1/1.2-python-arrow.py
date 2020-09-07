#!/usr/bin/env python3
# https://pypi.org/project/arrow/
# Arrow is a Python library that offers a sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps. It implements and updates the datetime type, plugging gaps in functionality and providing an intelligent module API that supports many common creation scenarios.


import arrow
date = arrow.get('2020-01-18', 'YYYY-MM-DD')
print (date.shift(weeks=+6).format('MMM DD YYYY'))

utc = arrow.utcnow()
print (utc)

currenttime = arrow.now()
print(currenttime)

print (currenttime.year)
