money_saved = 0

while True:
    destination = input()

    if destination == 'End':
        break

    minimum_money = float(input())
    money_saved = 0

    while money_saved < minimum_money:
        saved = float(input())
        money_saved += saved

    print(f'Going to {destination}!')