budget = int(input())
season = input()
group = int(input())

total = 0

if season == "Spring":
    if group <= 6:
        total = 0.9 * 3000
    elif 6 < group <= 11:
        total = 0.85 * 3000
    elif group >= 12:
        total = 0.75 * 3000
    if group % 2 == 0:
        total = 0.95 * total

elif season == "Summer" or season == "Autumn":
    if group <= 6:
        total = 0.9 * 4200
    elif 6 < group <= 11:
        total = 0.85 * 4200
    elif group >= 12:
        total = 0.75 * 4200
    if group % 2 == 0 and season == "Summer":
        total = 0.95 * total

elif season == "Winter":
    if group <= 6:
        total = 0.9 * 2600
    elif 6 < group <= 11:
        total = 0.85 * 2600
    elif group >= 12:
        total = 0.75 * 2600
    if group % 2 == 0:
        total = 0.95 * total

budget_left = budget - total

if budget_left >= 0:
    print(f"Yes! You have {abs(budget_left):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget_left):.2f} leva.")
