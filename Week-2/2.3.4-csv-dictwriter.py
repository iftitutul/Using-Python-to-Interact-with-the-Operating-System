#CSV stands for Comma Separated Values.

#!/usr/bin/env python3

import csv

users = [
         {
            "name":"Sol Mansi", 
            "username": "solm",
            "department": "IT Infra"
          },
         {
            "name": "Lio Nelson",
            "username": "lion",
            "department": "Developer"
         },
         {
            "name": "Charlie Grey",
            "username": "greyc",
            "department": "QA"  
         }
         ]

keys = ["name", "username", "department"]
with open("department.csv","w") as department:
   writer = csv.DictWriter(department,fieldnames=keys)
   writer.writeheader()
   writer.writerows(users)
