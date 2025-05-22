budget = float(input())
flour_price = float(input())
egg_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
milk_recipe = 0.25 * milk_price
minimum_money = egg_price + flour_price + milk_recipe

remaining_budget = budget
loafs_made = 0
eggs_earned = 0

while remaining_budget > minimum_money:

    remaining_budget = remaining_budget - egg_price - flour_price - milk_recipe
    loafs_made += 1
    eggs_earned += 3

    if loafs_made % 3 == 0:
        eggs_earned = eggs_earned - (loafs_made - 2)

print(f"You made {loafs_made} loaves of Easter bread! Now you have {eggs_earned} eggs and {remaining_budget:.2f}BGN left.")