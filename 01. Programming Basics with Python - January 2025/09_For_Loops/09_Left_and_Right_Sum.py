n = int(input())

right_sum = 0
left_sum = 0

for i in range(2):
    for _ in range(n):
        number = int(input())

        if i % 2 != 0:
            right_sum += number
        else:
            left_sum += number

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")
