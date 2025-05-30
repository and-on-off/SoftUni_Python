money_as_str = input().split(", ")
number_of_beggars = int(input())
money_as_int = []
# money_as_int = [int(money) for money in money_as_str]

for money in money_as_str:
    money_as_int.append(int(money))

final_list = []
start_index = 0

for beggar in range(number_of_beggars):
    beggar_sum = 0

    for index in range(start_index, len(money_as_int), number_of_beggars):
        beggar_sum += money_as_int[index]

    final_list.append(beggar_sum)
    start_index += 1


print(final_list)