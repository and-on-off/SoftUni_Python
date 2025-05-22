budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

costs = 0

if season == "Winter":
    if destination == "Dubai":
        costs = 45000 * number_of_days
    elif destination == "Sofia":
        costs = 17000 * number_of_days
    elif destination == "London":
        costs = 24000 * number_of_days

elif season == "Summer":
    if destination == "Dubai":
        costs = 40000 * number_of_days
    elif destination == "Sofia":
        costs = 12500 * number_of_days
    elif destination == "London":
        costs = 20250 * number_of_days

if destination == "Dubai":
    costs -= costs * 0.3
elif destination == "Sofia":
    costs += costs * 0.25

diff_sum = abs(budget - costs)

if budget >= costs:
    print(f"The budget for the movie is enough! We have {diff_sum:.2f} leva left!")
else:
    print(f"The director needs {diff_sum:.2f} leva more!")