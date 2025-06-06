def calculate_factorial(num: int) -> int:
    for current in range(1, num):
        num *= current
    return num

number1 = int(input())
number2 = int(input())
factorial1 = calculate_factorial(number1)
factorial2 = calculate_factorial(number2)
print(f"{factorial1 / factorial2:.2f}")