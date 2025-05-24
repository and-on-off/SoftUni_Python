number = int(input())
is_prime = True

for multiplier_one in range(2, number):
    for multiplier_two in range(2, number):
        if multiplier_one * multiplier_two == number:
            is_prime = False
        else:
            continue

print(is_prime)