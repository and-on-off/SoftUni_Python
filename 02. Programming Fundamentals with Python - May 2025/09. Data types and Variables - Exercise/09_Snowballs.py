snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality

    if value > max_value:
        max_value = value
        max_quality = quality
        max_time = time
        max_weight = weight

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
