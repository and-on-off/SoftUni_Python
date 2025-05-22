budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_price = 250
processor_price = 0.35 * (video_cards * video_price)
ram_price = 0.1 * (video_cards * video_price)

total_price = (video_cards * video_price) + (processors * processor_price) + (ram_memory * ram_price)

if video_cards > processors:
    total_price *= 0.85

if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")

elif budget < total_price:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
