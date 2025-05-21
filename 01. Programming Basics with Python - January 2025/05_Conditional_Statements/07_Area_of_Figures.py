import math

figure = str(input())

if figure == "square":
    side = float(input())
    print(f"{side.__pow__(2):.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    print(f"{side_a * side_b:.3f}")
elif figure == "circle":
    radius = float(input())
    print(f"{math.pi * radius.__pow__(2):.3f}")
elif figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    print(f"{0.5 * side_a * side_b:.3f}")
