def password_validator(some_password: str) -> list:
    errors_list = []
    if len(some_password) not in range(6, 10+1):
        errors_list.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        errors_list.append("Password must consist only of letters and digits")
    digit_counter = 0
    for symbol in some_password:
        if symbol.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        errors_list.append("Password must have at least 2 digits")

    return errors_list

password = input()
error_messages = password_validator(password)

if not error_messages:
    print("Password is valid")
else:
    print("\n".join(error_messages))