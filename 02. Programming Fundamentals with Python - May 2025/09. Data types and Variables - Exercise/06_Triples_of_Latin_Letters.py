# Variant 1
n = int(input())

for i in range(0, n):
    for k in range(0, n):
        for j in range(0, n):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")

# Variant 2
n = int(input())

for i in range(97, 97 + n):
    for k in range(97, 97 + n):
        for j in range(97, 97 + n):
            print(f"{chr(i)}{chr(k)}{chr(j)}")