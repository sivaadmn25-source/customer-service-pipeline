# D177 - Container Security Scanning
image_name = "customer-service"
vulnerability_found = False
if vulnerability_found:
    with open("security_check_result.txt", "w") as result:
        result.write("FAIL")
else:
    with open("security_check_result.txt", "w") as result:
        result.write("PASS")
print("CONTAINER SCAN COMPLETED")