import requests
import os

arr = [
        "bot.py",
        "modules/cmds.py",
        "modules/color.py",
        "modules/td.json",
        "modules/chelp.py"
        ]
pref = "https://venom-instantdeath.github.io/hkpages/priv/Tux/"

os.mkdir("modules")
open("modules/__init__.py", "w+").close()

for i in arr:
    print(f"Downloading {i}")
    r = requests.get(f"{pref}/{i}")
    f = open(i, "w+")
    f.write(r.text)
    f.close()

print("\nDone downloading!\n")
