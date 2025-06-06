def is_palindrome(some_number: str) -> bool:
    return some_number == some_number[::-1]

number_list = input().split(", ")

for number in number_list:
    print(is_palindrome(number))