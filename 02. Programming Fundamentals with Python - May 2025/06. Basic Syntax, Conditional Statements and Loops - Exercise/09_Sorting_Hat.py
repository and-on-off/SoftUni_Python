welcome_flag = False

while True:
    name = input()

    if name == "Welcome!":
        welcome_flag = True
        break

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")

    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")

    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")

    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

if welcome_flag:
    print("Welcome to Hogwarts.")