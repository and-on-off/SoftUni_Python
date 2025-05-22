string = input()
capital_indexes = []

for i, char in enumerate(string):
    if char.isupper():
        capital_indexes.append(i)

print(capital_indexes)
