#CSV stands for Comma Separated Values.

#!/usr/bin/env python3

import csv

f = open("csv_file.csv")
csv_file = csv.reader(f)
for row in csv_file:
   name, phone, role = row
   print("Name:{}, Phone: {}, Role: {}".format(name,phone,role))


f.close()
