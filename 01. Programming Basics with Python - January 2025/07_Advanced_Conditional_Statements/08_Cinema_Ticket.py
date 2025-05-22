day_of_week = input()

prices = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16,
}

if day_of_week in prices:
    print(prices[day_of_week])
