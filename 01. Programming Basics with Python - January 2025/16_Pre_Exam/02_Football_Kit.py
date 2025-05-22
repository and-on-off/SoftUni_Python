tshirt_price = float(input())
prize = float(input())
shorts_price = 0.75 * tshirt_price
socks_price = 0.20 * shorts_price
shoes_price = (tshirt_price + shorts_price) * 2


total_price = (tshirt_price + shorts_price + socks_price + shoes_price) * 0.85

if total_price >= prize:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")

else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {abs(prize - total_price):.2f} lv. more.")