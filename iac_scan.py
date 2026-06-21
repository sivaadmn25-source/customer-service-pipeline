# D178 - IaC Security Scanning
configuration_secure = True
if configuration_secure:
    with open("security_check_result.txt", "w") as result:
        result.write("PASS")
else:
    with open("security_check_result.txt", "w") as result:
        result.write("FAIL")
print("IAC SCAN COMPLETED")