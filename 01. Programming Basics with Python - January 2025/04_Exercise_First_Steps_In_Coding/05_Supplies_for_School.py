pen_pack = 5.80
marker_pack = 7.20
cleaner_per_litter = 1.20  # per liter

pens = int(input())
markers = int(input())
cleaner = int(input()) * cleaner_per_litter
discount = int(input()) / 100

sum_pen = pen_pack * pens
sum_markers = marker_pack * markers

result = sum_pen + sum_markers + cleaner
print(result - (result * discount))
