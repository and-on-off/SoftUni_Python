budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_add_costs = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95

price_for_all_period = number_of_nights * price_per_night
additional_costs = budget * (percent_add_costs / 100)
total_costs = price_for_all_period + additional_costs

diff_sum = abs(budget - total_costs)

if budget >= total_costs:
    print(f"Ivanovi will be left with {diff_sum:.2f} leva after vacation.")
else:
    print(f"{diff_sum:.2f} leva needed.")