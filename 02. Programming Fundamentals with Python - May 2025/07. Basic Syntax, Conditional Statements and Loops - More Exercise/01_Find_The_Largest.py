number = int(input())

digits = sorted(str(number), reverse=True)

print(int("".join(digits)))
