budget = float(input())
staff = int(input())
staff_costume = float(input()) * staff

decor = budget * 0.1

if staff >= 150:
    staff_costume *= 0.9

if decor + staff_costume > budget:
    money_needed = decor + staff_costume - budget
    print(f"Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

elif decor + staff_costume <= budget:
    money_left = budget - decor - staff_costume
    print(f"Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
