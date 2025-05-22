weight = float(input())
service = input()
distance = int(input())
price = 0
express_price = 0
total_price = 0

if service == "standard":
    if weight < 1:
        price = 0.03
    elif 1 <= weight < 10:
        price = 0.05
    elif 10 <= weight < 40:
        price = 0.10
    elif 40 <= weight < 90:
        price = 0.15
    elif 90 <= weight < 150:
        price = 0.20

    total_price = distance * price

elif service == "express":
    if weight < 1:
        price = 0.03
        express_price = price * 0.80
    elif 1 <= weight < 10:
        price = 0.05
        express_price = price * 0.40
    elif 10 <= weight < 40:
        price = 0.10
        express_price = price * 0.05
    elif 40 <= weight < 90:
        price = 0.15
        express_price = price * 0.02
    elif 90 <= weight < 150:
        price = 0.20
        express_price = price * 0.01

    total_price = (distance * price) + (distance * (weight * express_price))

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
