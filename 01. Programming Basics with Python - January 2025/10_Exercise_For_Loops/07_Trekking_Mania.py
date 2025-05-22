groups = int(input())
people_count = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for _ in range(groups):
    group_size = int(input())

    people_count += group_size

    if group_size <= 5:
        g1 += group_size
    elif 6 <= group_size <= 12:
        g2 += group_size
    elif 13 <= group_size <= 25:
        g3 += group_size
    elif 26 <= group_size <= 40:
        g4 += group_size
    elif group_size >= 41:
        g5 += group_size

print(f"{g1 / people_count * 100:.2f}%")
print(f"{g2 / people_count * 100:.2f}%")
print(f"{g3 / people_count * 100:.2f}%")
print(f"{g4 / people_count * 100:.2f}%")
print(f"{g5 / people_count * 100:.2f}%")