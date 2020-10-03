#CSV stands for Comma Separated Values.

#!/usr/bin/env python3

import csv

hosts = [["workstation.local", "192.168.1.24"], ["db.local", "192.168.1.200"], ["web.local","192.168.1.32"]]
with open("hosts.csv","w") as hosts_csv:
   writer = csv.writer(hosts_csv)
   writer.writerows(hosts)