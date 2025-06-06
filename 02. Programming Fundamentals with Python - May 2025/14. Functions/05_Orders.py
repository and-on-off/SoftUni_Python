product = input()
quantity = int(input())

def calculate_order(item: str, qty: int) -> float | None:
    if item == "coffee":
        return qty * 1.50
    elif item == "coke":
        return qty * 1.40
    elif item == "water":
        return qty * 1.00
    elif item == "snacks":
        return qty * 2.00
    return None

print(f"{calculate_order(product, quantity):.2f}")