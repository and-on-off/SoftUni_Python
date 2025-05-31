n = int(input())
word = input()

data_list = []

for _ in range(n):
    data_list.append(input())

print(data_list)
list_modified = data_list[:]

for element in data_list:
    if word not in element:
        list_modified.remove(element)

print(list_modified)