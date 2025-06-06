def even_numbers(number: int) -> bool:
    return number % 2 == 0

numbers_as_string = input().split()
numbers = []

for num in numbers_as_string:
    numbers.append(int(num))

final_result = filter(even_numbers, numbers)
print(list(final_result))