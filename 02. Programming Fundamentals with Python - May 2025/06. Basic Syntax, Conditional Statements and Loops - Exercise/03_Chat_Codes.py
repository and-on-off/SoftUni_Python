n = int(input())

for _ in range(n):
    code = int(input())
    message = ''

    if code == 88:
        message = "Hello"
    elif code == 86:
        message = "How are you?"
    elif code < 88:
        message = "GREAT!"
    elif code > 88:
        message = "Bye."
