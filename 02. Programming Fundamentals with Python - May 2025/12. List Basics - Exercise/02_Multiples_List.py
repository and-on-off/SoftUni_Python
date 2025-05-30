factor = int(input())
count = int(input())

multiples_list = []

for index in range(1, count + 1):

    multiples_list.append(index * factor)

print(multiples_list)