# D171 - Canary Deployment
from pathlib import Path
traffic_file = Path("traffic_distribution.txt")
values = {}
for line in traffic_file.read_text().splitlines():
    key, value = line.split("=")
    values[key] = int(value)
old_percent = values["OLD_VERSION"]
new_percent = values["NEW_VERSION"]
if old_percent >= 10:
    old_percent -= 10
    new_percent += 10
else:
    old_percent = 0
    new_percent = 100
traffic_file.write_text(
    f"OLD_VERSION={old_percent}\nNEW_VERSION={new_percent}"
)
print(f"OLD_VERSION={old_percent}%")
print(f"NEW_VERSION={new_percent}%")