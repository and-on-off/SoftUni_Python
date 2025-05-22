coins_counter = 0

amount = float(input())

while amount > 0:

    if amount - 2 >= 0:
        coins_counter += 1
        amount = round((amount - 2), 2)
    elif amount - 1 >= 0:
        coins_counter += 1
        amount = round((amount - 1), 2)
    elif amount - 0.50 >= 0:
        coins_counter += 1
        amount = round((amount - 0.50), 2)
    elif amount - 0.20 >= 0:
        coins_counter += 1
        amount = round((amount - 0.20), 2)
    elif amount - 0.10 >= 0:
        coins_counter += 1
        amount = round((amount - 0.10), 2)
    elif amount - 0.05 >= 0:
        coins_counter += 1
        amount = round((amount - 0.05), 2)
    elif amount - 0.02 >= 0:
        coins_counter += 1
        amount = round((amount - 0.02), 2)
    elif amount - 0.01 >= 0:
        coins_counter += 1
        amount = round((amount - 0.01), 2)

    if amount <= 0:
        break

print(coins_counter)