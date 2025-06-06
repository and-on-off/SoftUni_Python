def get_all_characters(first: str, second: str) -> list:
    characters = []
    for char in range(ord(first) + 1, ord(second)):
        characters.append(chr(char))
    return characters

char1 = input()
char2 = input()

characters_between = get_all_characters(char1, char2)

print(" ".join(characters_between))