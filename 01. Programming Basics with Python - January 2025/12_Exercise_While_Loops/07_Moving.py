width = int(input())
length = int(input())
height = int(input())
volume = width * length * height

while True:
    command = input()

    if command == "Done":
        print(f"{volume} Cubic meters left.")
        break

    boxes = int(command)
    volume -= boxes

    if volume < 0:
        print(f"No more free space! You need {abs(volume)} Cubic meters more.")
        break