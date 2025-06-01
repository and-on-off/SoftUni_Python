gifts_to_buy = input().split()
result_list = gifts_to_buy[:]

command = input()
while command != "No Money":
    command_as_list = command.split()

    if command_as_list[0] == "OutOfStock":
        result_list = [v.replace(command_as_list[1], "None") for v in gifts_to_buy]

    elif command_as_list[0] == "Required":
        if len(gifts_to_buy) > int(command_as_list[2]) >= 0:
            result_list[int(command_as_list[2])] = command_as_list[1]

    elif command_as_list[0] == "JustInCase":
        result_list[-1] = command_as_list[1]

    command = input()
    gifts_to_buy = result_list[:]

result_list = []
for item in gifts_to_buy:
    if item != "None":
        result_list.append(item)

print(" ".join(result_list))