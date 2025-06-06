def smallest_number(num1: int, num2: int, num3: int) -> int:
    list_of_numbers = [num1, num2, num3]
    return min(list_of_numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number, second_number, third_number))