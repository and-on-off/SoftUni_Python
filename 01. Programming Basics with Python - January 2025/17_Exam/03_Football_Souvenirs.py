team = input()
souvenirs = input()
souvenirs_bought = int(input())
total_price = 0

if team == "Argentina":
    if souvenirs == "flags":
        total_price = souvenirs_bought * 3.25
    elif souvenirs == "caps":
        total_price = souvenirs_bought * 7.20
    elif souvenirs == "posters":
        total_price = souvenirs_bought * 5.10
    elif souvenirs == "stickers":
        total_price = souvenirs_bought * 1.25

elif team == "Brazil":
    if souvenirs == "flags":
        total_price = souvenirs_bought * 4.20
    elif souvenirs == "caps":
        total_price = souvenirs_bought * 8.50
    elif souvenirs == "posters":
        total_price = souvenirs_bought * 5.35
    elif souvenirs == "stickers":
        total_price = souvenirs_bought * 1.20

elif team == "Croatia":
    if souvenirs == "flags":
        total_price = souvenirs_bought * 2.75
    elif souvenirs == "caps":
        total_price = souvenirs_bought * 6.90
    elif souvenirs == "posters":
        total_price = souvenirs_bought * 4.95
    elif souvenirs == "stickers":
        total_price = souvenirs_bought * 1.10

elif team == "Denmark":
    if souvenirs == "flags":
        total_price = souvenirs_bought * 3.10
    elif souvenirs == "caps":
        total_price = souvenirs_bought * 6.50
    elif souvenirs == "posters":
        total_price = souvenirs_bought * 4.80
    elif souvenirs == "stickers":
        total_price = souvenirs_bought * 0.90

if team not in ["Argentina", "Brazil", "Croatia", "Denmark"]:
    print(f"Invalid country!")
elif souvenirs not in ["flags", "caps", "posters", "stickers" ]:
    print(f"Invalid stock!")
else:
    print(f"Pepi bought {souvenirs_bought} {souvenirs} of {team} for {total_price:.2f} lv.")