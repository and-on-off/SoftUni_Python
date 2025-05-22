n = int(input())

for num in range(1, n + 1):
    digit_sum = 0

    for digits in str(num):
        digit_sum += int(digits)
    print(f"{num} -> {digit_sum == 5 or digit_sum == 7 or digit_sum == 11}")