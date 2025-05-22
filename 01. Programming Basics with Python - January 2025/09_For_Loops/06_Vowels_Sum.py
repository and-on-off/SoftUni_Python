text = input()

char_sum = 0

characters = {
    "a":1,
    "e":2,
    "i":3,
    "o":4,
    "u":5,
}

for char in text:
    if char in characters:
        char_sum += characters[char]

print(char_sum)
