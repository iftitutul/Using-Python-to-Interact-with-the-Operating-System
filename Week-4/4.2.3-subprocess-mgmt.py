#!/usr/bin/env python3.6

import subprocess
import os

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])

result = subprocess.run(["myapp"], env= my_env)