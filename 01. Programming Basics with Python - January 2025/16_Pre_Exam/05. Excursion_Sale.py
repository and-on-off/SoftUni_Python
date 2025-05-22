sea_tours = int(input())
mountain_tours = int(input())
profit = 0

while True:

    command = input()

    if command == "Stop":
        break

    if command == "sea" and sea_tours > 0:
        profit += 680
        sea_tours -= 1
    elif command == "mountain" and mountain_tours > 0:
        profit += 499
        mountain_tours -= 1
    if sea_tours == 0 and mountain_tours == 0:
        print(f"Good job! Everything is sold.")
        break

print(f"Profit: {profit} leva.")
