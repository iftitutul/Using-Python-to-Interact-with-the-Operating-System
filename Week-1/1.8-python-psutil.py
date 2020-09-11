#!/usr/bin/env python3

import psutil

cpu_percent = psutil.cpu_percent(0.1)
print (cpu_percent)

cpu_count = psutil.cpu_count()
print (cpu_count)

