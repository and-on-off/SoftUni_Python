import sys

number = int(input())
sum_numbers = 0
max_num = -sys.maxsize

for _ in range(0, number):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_numbers += num

if max_num == sum_numbers - max_num:
    print(f"Yes\nSum = {max_num}")
else:
    sum_numbers -= max_num
    print(f"No\nDiff = {abs(max_num - sum_numbers)}")