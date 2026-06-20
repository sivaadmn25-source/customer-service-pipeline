# D168 - Environment Promotion
import glob
import os
import shutil
artifacts = glob.glob("customer-service-*.zip")
if not artifacts:
    raise FileNotFoundError("No artifacts found")
latest_artifact = max(artifacts, key=os.path.getmtime)
target = os.path.join("environments", "qa", os.path.basename(latest_artifact))
shutil.copy(latest_artifact, target)
print(f"PROMOTED TO QA: {os.path.basename(latest_artifact)}")