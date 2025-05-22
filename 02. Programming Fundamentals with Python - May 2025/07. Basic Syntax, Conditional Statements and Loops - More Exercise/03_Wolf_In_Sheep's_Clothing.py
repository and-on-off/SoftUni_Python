input_string = input()
listed = input_string.split(', ')
listed.reverse()

for i, word in enumerate(listed):
    if listed[0] == "wolf":
        print(f"Please go away and stop eating my sheep")
        break

    if word == "wolf":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
        break