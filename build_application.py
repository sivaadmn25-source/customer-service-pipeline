import shutil
import os

BUILD_DIR = "build_v1"

if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

os.makedirs(BUILD_DIR)

files_to_package = [
    "customer.dat",
    "read_customer.py"
]

for file in files_to_package:
    shutil.copy(file, BUILD_DIR)

print("BUILD COMPLETED")