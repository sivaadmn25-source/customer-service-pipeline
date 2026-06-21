# D173 - DevSecOps Integration

with open("security_check_result.txt", "r") as file:
    result = file.read().strip()

if result != "PASS":
    raise Exception("SECURITY GATE FAILED")

print("SECURITY GATE PASSED")