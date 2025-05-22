locations = int(input())
average_grind_per_day = 0
day_counter = 0

for location in range(1, locations + 1):
    average_daily_grind = float(input())
    days_grinding = int(input())

    for day in range(1, days_grinding + 1):
        daily_grind = float(input())
        average_grind_per_day += daily_grind
        day_counter += 1

    average_grind_per_day = average_grind_per_day / day_counter
    if average_grind_per_day >= average_daily_grind:
        print(f"Good job! Average gold per day: {average_grind_per_day:.2f}.")
        average_grind_per_day = 0
        day_counter = 0
    else:
        print(f"You need {average_daily_grind - average_grind_per_day:.2f} gold.")
        average_grind_per_day = 0
        day_counter = 0


