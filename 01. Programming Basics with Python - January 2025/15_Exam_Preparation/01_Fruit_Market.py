strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.60
banana_price = raspberry_price * 0.20

total_price = ((raspberry_price * raspberry_quantity) + (orange_price * orange_quantity) +
               (banana_price * banana_quantity) + (strawberry_price * strawberry_quantity))

print(f"{total_price:.2f}")

