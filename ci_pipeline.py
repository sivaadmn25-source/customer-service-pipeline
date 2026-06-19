import subprocess
import sys

print("STAGE 1 - TESTS")

result = subprocess.run(["python", "run_tests.py"])

if result.returncode != 0:
    print("PIPELINE FAILED AT TEST STAGE")
    sys.exit(1)

print("STAGE 2 - BUILD")

result = subprocess.run(["python", "build_application.py"])

if result.returncode != 0:
    print("PIPELINE FAILED AT BUILD STAGE")
    sys.exit(1)

print("STAGE 3 - ARTIFACT")

result = subprocess.run(["python", "create_artifact.py"])

if result.returncode != 0:
    print("PIPELINE FAILED AT ARTIFACT STAGE")
    sys.exit(1)

print("STAGE 4 - DEPLOY")
result = subprocess.run(["python", "deploy_application.py"])

if result.returncode != 0:
    print("PIPELINE FAILED AT DEPLOY STAGE")
    sys.exit(1)

print("PIPELINE COMPLETED SUCCESSFULLY")