# Вариант 1 - работи за конкретната задача

number = int(input())

if number < 100:
    print("Less than 100")
elif number > 200:
    print("Greater than 200")
else:
    print("Between 100 and 200")



# Моята логика - очевидно невярна (Whyyyyy)
number = int(input())

if number < 100:
    print("Less than 100")
elif number >= 100 & number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")




# Вариант 2:
number = int(input())

if number < 100:
    print("Less than 100")
elif 100 <= number <= 200: # <--- Ight Imma Head Out
    print("Between 100 and 200")
else:
    print("Greater than 200")
