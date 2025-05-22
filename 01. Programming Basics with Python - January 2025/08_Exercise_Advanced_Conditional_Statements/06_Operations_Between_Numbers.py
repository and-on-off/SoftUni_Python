n1 = int(input())
n2 = int(input())
operator = input()
result = 0


def is_even(number):
    return "even" if number % 2 == 0 else "odd"


if operator in ["+", "-", "*"]:
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    odd_even = is_even(result)
    print(f"{n1} {operator} {n2} = {result} - {odd_even}")

elif operator in ["/", "%"]:
    division_zero = 0
    if n1 != 0 and n2 != 0:
        if operator == "/":
            print(f"{n1} {operator} {n2} = {n1 / n2:.2f}")
        elif operator == "%":
            print(f"{n1} {operator} {n2} = {n1 % n2}")
    elif n1 == 0 or n2 == 0:
        if n1 > n2:
            division_zero = n1
        else:
            division_zero = n2
        print(f"Cannot divide {division_zero} by zero")
