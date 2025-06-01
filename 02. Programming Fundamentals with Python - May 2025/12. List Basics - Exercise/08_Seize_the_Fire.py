input_list = input().split("#")
water_amount = int(input())
effort = 0
fire_and_cells = []
cells_putout = []
options = ["High", "Medium", "Low"]


for fc in range(len(input_list)):
    fire_and_cells.append(input_list[fc].split(" = "))

for f_and_c in fire_and_cells:
    if (f_and_c[0] == "Low" and 1 <= int(f_and_c[1]) <= 50) or \
        (f_and_c[0] == "Medium" and 51 <= int(f_and_c[1]) <= 80) or \
        (f_and_c[0] == "High" and 81 <= int(f_and_c[1]) <= 125):
            if int(f_and_c[1]) <= water_amount:
                water_amount -= int(f_and_c[1])
                effort += int(f_and_c[1]) * 0.25
                cells_putout.append(int(f_and_c[1]))

print("Cells:")
for cell in cells_putout:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells_putout)}")