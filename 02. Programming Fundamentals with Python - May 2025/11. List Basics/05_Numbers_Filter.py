n = int(input())
numbers = []
filtered_numbers = []
command_options = ['even', 'odd', 'negative', 'positive']

for _ in range(n):
    num = int(input())
    numbers.append(num)

command = input()

if command == 'even':
    filtered_numbers = [element for element in numbers if element == 0 or element % 2 == 0]
    # for element in numbers:
    #     if element == 0 or element % 2 == 0:
    #         filtered_numbers.append(element)
elif command == 'odd':
    filtered_numbers = [element for element in numbers if element % 2 != 0]
    # for element in numbers:
    #     if element % 2 != 0:
    #         filtered_numbers.append(element)
elif command == 'negative':
    filtered_numbers = [element for element in numbers if element < 0]
    # for element in numbers:
    #     if element < 0:
    #         filtered_numbers.append(element)
elif command == 'positive':
    filtered_numbers = [element for element in numbers if element >= 0]
    # for element in numbers:
    #     if element >= 0:
    #         filtered_numbers.append(element)

print(filtered_numbers)

