puzzle = 2.6
doll = 3
bear = 4.1
minion = 8.2
truck = 2

vacation_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bears_count = int(input())
minion_count = int(input())
truck_count = int(input())

order = puzzle_count + doll_count + bears_count + minion_count + truck_count
total_price = puzzle_count * puzzle + doll_count * doll + bears_count * bear + minion_count * minion + truck_count * truck

if order >= 50:
    total_price *= 0.75

total_price *= 0.9

if total_price >= vacation_price:
    total_price -= vacation_price
    print(f"Yes! {total_price:.2f} lv left.")

elif total_price < vacation_price:
    vacation_price -= total_price
    print(f"Not enough money! {vacation_price:.2f} lv needed.")
