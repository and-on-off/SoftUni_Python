cake_width = int(input())
cake_length = int(input())
cake_size = cake_width * cake_length
take_counter = 0

while cake_size >= 0:
    take = input()

    if take == "STOP":
        break

    cake_size -= int(take)

if cake_size > 0:
    print(f"{cake_size} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")