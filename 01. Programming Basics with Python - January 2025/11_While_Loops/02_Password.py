username = input()
password = input()

while True:
    user_pass = input()

    if user_pass == password:
        print(f"Welcome {username}!")
        break
