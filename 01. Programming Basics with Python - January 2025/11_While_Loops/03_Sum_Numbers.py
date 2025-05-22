last_number = int(input())
sum_number = 0

while True:
    number = int(input())
    sum_number += number
    if sum_number >= last_number:
        break
print(sum_number)