# Variant 1

tail = input()
body = input()
head = input()

meerkat = [head, body, tail]

print(meerkat)

# Variant 2

meerkat = []

for i in range(3):
    data = input()
    meerkat.append(data)

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)