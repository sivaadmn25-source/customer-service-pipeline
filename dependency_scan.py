# D175 - Dependency Scanning
with open("dependencies.txt", "r") as file:
    dependencies = file.read()
if "log4j" in dependencies.lower():
    with open("security_check_result.txt", "w") as result:
        result.write("FAIL")
else:
    with open("security_check_result.txt", "w") as result:
        result.write("PASS")
print("DEPENDENCY SCAN COMPLETED")