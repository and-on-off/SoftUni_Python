input_list = input().split()

opposite_list = []

for value in input_list:
    value_as_number = int(value)

    opposite_list.append(-value_as_number)

print(opposite_list)