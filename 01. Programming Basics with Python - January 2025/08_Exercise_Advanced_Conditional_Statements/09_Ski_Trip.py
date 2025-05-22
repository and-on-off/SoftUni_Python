days = int(input())
hotel_type = input()
rate = input()
nights = days - 1
single_room = 18 # per night
apartment = 25 # per night
president = 35 # per night
total_price = 0

if hotel_type == "room for one person":
    total_price = single_room * nights

elif hotel_type == "apartment":
    total_price = apartment * nights

    if days < 10:
        total_price *= 0.7

    elif 10 <= days <= 15:
        total_price *= 0.65

    elif days > 15:
        total_price *= 0.5

elif hotel_type == "president apartment":
    total_price = president * nights

    if days < 10:
        total_price *= 0.9

    elif 10 <= days <= 15:
        total_price *= 0.85

    elif days > 15:
        total_price *= 0.8

if rate == "positive":
    total_price *= 1.25

elif rate == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")
