# shoes = 40% less than tax
# equipment = 20% less than shoes
# ball = 25% from equipment
# accessories = 20% from ball
# tax = input()

tax = int(input())

shoes = tax * 0.60
equipment = shoes * 0.80
ball = equipment * 0.25
accessories = ball * 0.20

result = tax + shoes + equipment + ball + accessories
print(result)
