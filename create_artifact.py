# D167 - Artifact Versioning
import os
import shutil
VERSION = "1.0.0"
BUILD_NUMBER = os.getenv("BUILD_NUMBER", "LOCAL")
ARTIFACT_NAME = f"customer-service-{VERSION}-build-{BUILD_NUMBER}"
shutil.make_archive(
    ARTIFACT_NAME,
    "zip",
    "build_v1"
)
print(f"ARTIFACT CREATED: {ARTIFACT_NAME}.zip")