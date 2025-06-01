import sys

input_numbers = input().split()
n = int(input())
numbers = []

for num in input_numbers:
    numbers.append(int(num))

for cycle in range(n):
    smallest_integer = sys.maxsize
    for index in numbers:
        if index < smallest_integer:
            smallest_integer = index
    numbers.remove(smallest_integer)

print(", ".join(list(map(str, numbers))))