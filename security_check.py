# D172 - Pipeline Security (RBAC)

roles = {}

with open("user_roles.txt", "r") as file:
    for line in file:
        user, role = line.strip().split("=")
        roles[user] = role

request = {}

with open("deployment_request.txt", "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        request[key] = value

user = request["USER"]
target_env = request["TARGET_ENV"]

if user not in roles:
    print(f"ACCESS DENIED: {user}")

else:

    role = roles[user]

    if target_env == "production" and role != "release_manager":
        print(
            f"DEPLOYMENT DENIED: {user} ({role}) cannot deploy to production"
        )

    else:
        print(
            f"DEPLOYMENT APPROVED: {user} ({role}) -> {target_env}"
        )