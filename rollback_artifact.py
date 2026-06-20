# D169 - Rollback Strategy
from pathlib import Path
production_file = Path("production_version.txt")
current_version = production_file.read_text().strip()
available_versions = sorted(
    [f.name for f in Path("environments/production").glob("customer-service-*.zip")]
)
current_index = available_versions.index(current_version)
if current_index == 0:
    raise Exception("No previous version available for rollback")
rollback_version = available_versions[current_index - 1]
production_file.write_text(rollback_version)
print(f"CURRENT VERSION : {current_version}")
print(f"ROLLED BACK TO  : {rollback_version}")