start_interval = int(input())
final_interval = int(input())
magic_num = int(input())
counter = 0
flag = False

for x in range(start_interval, final_interval + 1):
    for y in range(start_interval, final_interval + 1):
        counter += 1
        if x + y == magic_num:
            print(f"Combination N:{counter} ({x} + {y} = {magic_num})")
            flag = True
            break

    if flag:
        break
else:
    print(f"{counter} combinations - neither equals {magic_num}")