from math import ceil

series_name = str(input())
episode_duration = int(input())
duration_lunch = int(input())

lunch_time = duration_lunch / 8
break_time = duration_lunch / 4

time_left = duration_lunch - (episode_duration + lunch_time + break_time)

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left):.0f} minutes free time.")
elif time_left < 0:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left)):.0f} more minutes.")
