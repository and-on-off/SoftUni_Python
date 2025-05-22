flower_type = input()
quantity = int(input())
budget = int(input())
total = 0

if flower_type == "Roses":
    if quantity > 80:
        total = 0.9*(quantity*5)
    else:
        total = quantity*5
elif flower_type == "Dahlias":
    if quantity > 90:
        total = 0.85*(quantity*3.8)
    else:
        total = quantity*3.8
elif flower_type == "Tulips":
    if quantity > 80:
        total = 0.85*(quantity*2.8)
    else:
        total = quantity*2.8
elif flower_type == "Narcissus":
    if quantity < 120:
        total = 1.15*(quantity*3)
    else:
        total = quantity*3
elif flower_type == "Gladiolus":
    if quantity < 80:
        total = 1.2*(quantity*2.5)
    else:
        total = quantity*2.5

budget -= total

if budget >= 0:
    print(f"Hey, you have a great garden with {quantity} {flower_type} and {budget:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget):.2f} leva more.")
