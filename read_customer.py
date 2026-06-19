def parse_record(line):
    customer_id = line[0:6].strip()
    customer_name = line[6:26].strip()
    account_type = line[26:29].strip()
    balance = float(line[29:38].strip())
    return {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "account_type": account_type,
        "balance": balance
    }

def read_customers(filename):
    customers = []
    with open(filename, "r") as file:
        for line in file:
            customers.append(parse_record(line))
    return customers

if __name__ == "__main__":
    customers = read_customers("customer.dat")
    for customer in customers:
        print(customer)