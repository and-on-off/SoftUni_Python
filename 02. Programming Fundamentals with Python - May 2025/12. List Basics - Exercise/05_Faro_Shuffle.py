deck = input().split()
shuffles = int(input())

first_card = [deck.pop(0)]
last_card = [deck.pop(-1)]
faro_shuffle = []

for shuffle in range(shuffles):
    for card in range(int(len(deck) / 2)):
        half1 = deck[:len(deck) // 2]
        half2 = deck[len(deck) // 2:]
        faro_shuffle += half2[card], half1[card]
    deck = faro_shuffle
    faro_shuffle = []

print(first_card + deck + last_card)