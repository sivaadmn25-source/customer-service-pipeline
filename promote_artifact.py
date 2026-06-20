# D168 - Environment Promotion
import glob
import os
import shutil
artifacts = glob.glob("customer-service-*.zip")
if not artifacts:
    raise FileNotFoundError("No artifacts found")
artifact_name = max(artifacts, key=os.path.getmtime)
qa_target = os.path.join("environments", "qa", artifact_name)
uat_target = os.path.join("environments", "uat", artifact_name)
prod_target = os.path.join("environments", "production", artifact_name)
shutil.copy(artifact_name, qa_target)
print(f"PROMOTED TO QA: {artifact_name}")
shutil.copy(artifact_name, uat_target)
print(f"PROMOTED TO UAT: {artifact_name}")
shutil.copy(uat_target, prod_target)
print(f"PROMOTED TO PRODUCTION: {artifact_name}")