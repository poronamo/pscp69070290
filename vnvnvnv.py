"""bill"""

def main():
    """help"""
    bill = float(input())
    service = bill * 0.1
    vat = (bill + service) * 0.07
    if service < 50:
        print(f"{bill + service + vat:.2f}")
    elif service > 1000:
        print(f"{bill + service + vat:.2f}")
    else:
        print(f"{bill + service + vat:.2f}")
main()
