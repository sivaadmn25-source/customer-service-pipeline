import shutil
ARTIFACT_NAME = "customer-service-1.0.0"
shutil.make_archive(
    ARTIFACT_NAME,
    "zip",
    "build_v1"
)
print(f"ARTIFACT CREATED: {ARTIFACT_NAME}.zip")