player_one_eggs = int(input())
player_two_eggs = int(input())

while True:
    command = input()

    if command == "End":
        break

    elif command == "one":
        player_two_eggs -= 1

    elif command == "two":
        player_one_eggs -= 1

    if player_one_eggs <= 0 or player_two_eggs <= 0:
        break

if player_one_eggs <= 0:
    print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")

elif player_two_eggs <= 0:
    print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")

else:
    print(f"Player one has {player_one_eggs} eggs left.")
    print(f"Player two has {player_two_eggs} eggs left.")
