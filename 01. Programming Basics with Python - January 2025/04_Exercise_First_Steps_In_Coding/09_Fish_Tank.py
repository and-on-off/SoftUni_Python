length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
# 1 l = 10 cm3

gross_tank_volume = length * width * height  # in cm3
tank_volume = gross_tank_volume - (gross_tank_volume * percent)
litres = tank_volume * 0.001

print(litres)
