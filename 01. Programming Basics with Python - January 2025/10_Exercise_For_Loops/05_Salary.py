tabs_open = int(input())
salary = int(input())

for tab in range(tabs_open):
    site = input()

    if site == "Facebook":
        salary -= 150

    elif site == "Instagram":
        salary -= 100

    elif site == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary}")
