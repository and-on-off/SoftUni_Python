string = input().lower()
counter = 0
words_to_find = ["sand", "water", "fish", "sun"]

for word in words_to_find:
    counter += string.count(word)

print(counter)