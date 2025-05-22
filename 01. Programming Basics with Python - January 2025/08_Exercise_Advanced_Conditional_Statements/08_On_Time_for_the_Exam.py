exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
final_hours = 0
final_minutes = 0

exam = exam_hour * 60 + exam_minute
arrival = arrival_hour * 60 + arrival_minute

if arrival > exam: # Late
    if arrival <= (exam + 59):
        final_minutes = arrival - exam
        print("Late")
        print(f"{final_minutes} minutes after the start")
    else:
        final_hours = (arrival - exam) // 60
        final_minutes = (arrival - exam) % 60
        print("Late")
        print(f"{final_hours}:{final_minutes:02d} hours after the start")

elif (exam - 30) <= arrival <= exam: # On time
    if arrival == exam:
        print("On time")
    else:
        final_minutes = exam - arrival
        print("On time")
        print(f"{final_minutes} minutes before the start")

elif (exam - 30) > arrival: # Early
    if (arrival + 59) >= exam:
        final_minutes = exam - arrival
        print("Early")
        print(f"{final_minutes} minutes before the start")
    else:
        final_hours = abs((exam - arrival) // 60)
        final_minutes = abs((exam - arrival) % 60)
        print("Early")
        print(f"{final_hours}:{final_minutes:02d} hours before the start")
