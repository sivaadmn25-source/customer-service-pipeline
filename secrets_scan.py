# D176 - Secrets Scanning
files_to_scan = [
    "read_customer.py"
]
secret_found = False
for file_name in files_to_scan:
    with open(file_name, "r") as file:
        content = file.read()
        if "PASSWORD =" in content:
            secret_found = True
if secret_found:
    with open("security_check_result.txt", "w") as result:
        result.write("FAIL")
else:
    with open("security_check_result.txt", "w") as result:
        result.write("PASS")
print("SECRETS SCAN COMPLETED")