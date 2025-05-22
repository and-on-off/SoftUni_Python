food_bought = int(input())
available_food = food_bought * 1000

while True:
    command = input()
    if command == "Adopted":
        break

    food_eaten = int(command)

    available_food -= food_eaten


if available_food >= 0:
    print(f"Food is enough! Leftovers: {available_food} grams.")
else:
    print(f"Food is not enough. You need {abs(available_food)} grams more.")