#!/usr/bin/env python3
import pandas

vistors = [ 12123, 32334, 423134, 32432, 534343, 43424, 42555]
errors = [400, 200, 503, 500, 301, 200, 302]

df = pandas.DataFrame( {"Visitors": vistors, "Errors": errors}, index=["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"])

print (df)

print (f'Mean Value: {df["Errors"].mean()}')