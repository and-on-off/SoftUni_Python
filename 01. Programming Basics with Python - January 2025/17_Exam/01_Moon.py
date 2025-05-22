from math import ceil

average_speed = float(input())
fuel_consumption = float(input())

distance = 384400

total_distance = distance * 2
time_total_distance = ceil(total_distance / average_speed)
total_time = time_total_distance + 3

fuel = ((fuel_consumption * total_distance) / 100)

print(f"{ceil(total_time)}")
print(f"{fuel:.0f}")
