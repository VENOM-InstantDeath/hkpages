#!/usr/bin/env python3
import os
import subprocess


def get(p):
    x=subprocess.Popen(p+"x", shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return x.stdout.read(), x.stderr.read().decode()


print("Ruta del script (no incluye el script)")
p=input("Input path: ")
os.chdir(p)
if not p.endswith('/'): p+='/'
x, y = get(p)
print(f"\n\n\n\nSTDOUT: {x}\n\nSTDERR: {y}")
