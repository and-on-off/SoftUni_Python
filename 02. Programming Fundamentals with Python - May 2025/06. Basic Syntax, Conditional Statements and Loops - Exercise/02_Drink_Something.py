ages = int(input())
drink = ''

if ages <= 14:
    drink = 'toddy'

elif ages <= 18:
    drink = 'coke'

elif ages <= 21:
    drink = 'beer'

elif ages > 21:
    drink = 'whisky'

print(f"drink {drink}")
