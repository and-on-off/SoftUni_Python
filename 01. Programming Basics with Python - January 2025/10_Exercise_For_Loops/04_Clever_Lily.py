age = int(input())
washer_price = float(input())
toy_price = int(input())
available_money = 0
available_toys = 0
money_gift = 10

for year in range(1, age + 1):

    if year % 2 == 0:
        available_money += money_gift - 1
        money_gift += 10


    elif year % 2 != 0:
        available_toys += 1

available_money = available_money + available_toys * toy_price

if available_money >= washer_price:
    print(f"Yes! {available_money - washer_price:.2f}")

else:
    print(f"No! {washer_price - available_money:.2f}")