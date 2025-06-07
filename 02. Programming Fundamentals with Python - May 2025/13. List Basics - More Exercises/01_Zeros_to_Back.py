input_numbers = input().split(", ")
numbers = []
zeroes = []

for number in input_numbers:
    if int(number) == 0:
        zeroes.append(int(number))
    else:
        numbers.append(int(number))

print(numbers + zeroes)