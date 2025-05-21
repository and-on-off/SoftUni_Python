floor_cover = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

sum_materials = (floor_cover + 2) * 1.50\
                + paint_thinner * 5\
                + (paint + (paint * 0.1)) * 14.50\
                + 0.40

salary = (sum_materials * 0.3) * hours

print(sum_materials + salary)
