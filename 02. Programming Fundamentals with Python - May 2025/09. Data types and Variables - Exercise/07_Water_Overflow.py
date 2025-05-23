tank_capacity = 0
n = int(input())

for i in range(n):
    liters_of_water = int(input())

    if tank_capacity + liters_of_water > 255:
        print("Insufficient capacity!")
    else:
        tank_capacity += liters_of_water

print(tank_capacity)