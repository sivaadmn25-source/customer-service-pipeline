import subprocess
import sys

result = subprocess.run(
    ["pytest", "-v"],
    capture_output=True,
    text=True
)
print(result.stdout)
if result.returncode == 0:
    print("\nTEST EXECUTION SUCCESSFUL")
else:
    print("\nTEST EXECUTION FAILED")
    sys.exit(1)