days = int(input())
total_food_quantity = float(input())

total_cookies = 0
total_food_eaten = 0
total_food_dog_eaten = 0
total_food_cat_eaten = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_food_eaten += dog_food + cat_food

    if day % 3 == 0:
        total_cookies += (dog_food + cat_food) * 0.10

    total_food_dog_eaten += dog_food
    total_food_cat_eaten += cat_food

percent_cookies = round(total_cookies)
percent_food_eaten = (total_food_eaten / total_food_quantity) * 100
percent_dog_food_eaten = (total_food_dog_eaten / total_food_quantity) * 100
percent_cat_food_eaten = (total_food_cat_eaten / total_food_quantity) * 100

print(f"Total eaten biscuits: {percent_cookies}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog_food_eaten:.2f}% eaten from the dog.")
print(f"{percent_cat_food_eaten}% eaten from the cat.")