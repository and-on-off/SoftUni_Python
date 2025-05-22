product = input()
day_of_week = input()
quantity = float(input())

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

fruit_prices = {
    "banana": [2.50, 2.70],
    "apple": [1.20, 1.25],
    "orange": [0.85, 0.90],
    "grapefruit": [1.45, 1.60],
    "kiwi": [2.70, 3.00],
    "pineapple": [5.50, 5.60],
    "grapes": [3.85, 4.20]
}

if day_of_week in working_days and product in fruit_prices:
    print(f"{fruit_prices[product][0] * quantity:.2f}")
elif day_of_week in weekend and product in fruit_prices:
    print(f"{fruit_prices[product][1] * quantity:.2f}")
else:
    print("error")
