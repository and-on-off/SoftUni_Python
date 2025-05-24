key = int(input())
lines = int(input())
decrypted_message = ""

for char in range(lines):
    letter = input()
    decrypted_message += chr(ord(letter) + key)

print(decrypted_message)