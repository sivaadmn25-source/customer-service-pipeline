# D174 - SAST Integration (Static Application Security Testing)
files_to_scan = [
    "read_customer.py"
]
security_issue_found = False
for file_name in files_to_scan:
    with open(file_name, "r") as file:
        content = file.read()
        if "eval(" in content:
            print(f"SECURITY ISSUE FOUND IN {file_name}")
            security_issue_found = True
if security_issue_found:
    with open("security_check_result.txt", "w") as result:
        result.write("FAIL")
else:
    with open("security_check_result.txt", "w") as result:
        result.write("PASS")
print("SAST SCAN COMPLETED")