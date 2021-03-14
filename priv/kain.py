#!/usr/bin/env python3

import subprocess
p=input("Input path: ")
x=subprocess.Popen(path, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(f"\n\n\n\nSTDOUT: {x.stdout.read()}\n\nSTDERR: {x.stderr.read().decode()}")
