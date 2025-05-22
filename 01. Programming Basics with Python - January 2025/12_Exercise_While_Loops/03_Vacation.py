vacation_money = float(input())
available_money = float(input())
days_passed = 0
spend_counter = 0

while available_money < vacation_money and spend_counter < 5:
    action = input()
    money = float(input())

    if action == "save":
        available_money += money
        days_passed += 1
        spend_counter = 0

    elif action == "spend":
        available_money -= money
        if available_money < 0:
            available_money = 0
        days_passed += 1
        spend_counter += 1

if available_money >= vacation_money:
    print(f"You saved the money for {days_passed} days.")

else:
    print(f"You can't save the money.")
    print(f"{days_passed}")
