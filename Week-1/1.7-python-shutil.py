#!/usr/bin/env python3

import shutil

du = shutil.disk_usage("/")
print (du)

free_mb = du.free/du.total*100
print (f'disk free size in mb: {free_mb}')