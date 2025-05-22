tournaments_participated = int(input())
starting_points = int(input())
earned_points = 0
wins = 0

for _ in range(tournaments_participated):
    stage = input()

    if stage == "W":
        earned_points += 2000
        wins += 1

    elif stage == "F":
        earned_points += 1200

    elif stage == "SF":
        earned_points += 720

average_points = earned_points / tournaments_participated
wins_percent = wins / tournaments_participated * 100

print(f"Final points: {earned_points + starting_points}")
print(f"Average points: {int(average_points)}")
print(f"{wins_percent:.2f}%")