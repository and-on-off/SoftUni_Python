hours = int(input())
minutes = int(input())

total_minutes = (hours * 60) + minutes + 15

hour_time = total_minutes // 60
minute_time = total_minutes % 60

if hour_time >= 24:
    hour_time = 0

if minute_time < 10:
    print(f"{hour_time}:{minute_time:02d}")
else:
    print(f"{hour_time}:{minute_time}")

