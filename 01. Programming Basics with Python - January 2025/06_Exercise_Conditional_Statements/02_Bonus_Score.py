number = int(input())
bonus = 0

if number <= 100:
    bonus = 5

elif number > 1000:
    bonus = 0.1 * number

else:
    bonus = 0.2 * number

if number % 2 == 0:
    bonus += 1

elif number % 5 == 0:
    bonus += 2

print(bonus)
print(bonus + number)
