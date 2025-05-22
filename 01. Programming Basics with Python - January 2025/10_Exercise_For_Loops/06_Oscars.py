actor_name = input()
academy_points = float(input())
jury = int(input())
sum_points = academy_points

for _ in range(jury):
    jury_name = input()
    points = float(input())

    sum_points = sum_points + ((len(jury_name) * points) / 2)

    if sum_points >= 1250.5:
        break

if sum_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {sum_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - sum_points:.1f} more!")
