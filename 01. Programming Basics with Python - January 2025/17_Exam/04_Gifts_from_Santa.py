n = int(input())
m = int(input())
s = int(input())

for address in range(m, n - 1, -1):

    if address % 2 == 0 and address % 3 == 0:
        if s == address:
            break
        print(address, end=" ")
