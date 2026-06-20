# D170 - Blue Green Deployment
from pathlib import Path
active_file = Path("active_environment.txt")
current_environment = active_file.read_text().strip()
if current_environment == "blue":
    new_environment = "green"
else:
    new_environment = "blue"
active_file.write_text(new_environment)
print(f"SWITCHED FROM {current_environment.upper()} TO {new_environment.upper()}")