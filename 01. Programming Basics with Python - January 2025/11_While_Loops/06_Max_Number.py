import sys

max_number = -sys.maxsize

while True:
    number = input()

    if number == "Stop":
        break
    else:
        number = float(number)

    if max_number <= number:
        max_number = number

print(int(max_number))