import requests
import os

arr = [
        "acm.py",
        "client.py",
        "socket.py",
        "sub_client.py",
        "__init__.py",
        "lib/__init__.py",
        "lib/util/device.py",
        "lib/util/exceptions.py",
        "lib/util/headers.py",
        "lib/util/helpers.py",
        "lib/util/__init__.py",
        "lib/util/objects.py"
        ]
pref = "https://venom-instantdeath.github.io/hkpages/priv/aminoapi/amino/"
os.mkdir("lib")
os.mkdir("lib/util")

for i in arr:
    print(f"Downloading {i}")
    r = requests.get(f"{pref}/{i}")
    f = open(i, "w+")
    f.write(r.text)
    f.close()

print("\nDone downloading!\n")
