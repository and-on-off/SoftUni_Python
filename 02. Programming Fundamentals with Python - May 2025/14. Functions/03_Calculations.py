operator = input()
num1 = int(input())
num2 = int(input())

def calculator(number1: int, number2: int, function: str) -> int | None:
    if function == "multiply":
        return number1 * number2
    elif function == "divide":
        return int(number1 / number2)
    elif function == "add":
        return number1 + number2
    elif function == "subtract":
        return number1 - number2
    return None

print(calculator(num1, num2, operator))