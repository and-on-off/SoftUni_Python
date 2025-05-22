current_record = float(input())
distance = float(input())
meter_swimming_time = float(input())

time_needed = distance * meter_swimming_time
time_add = (distance // 15) * 12.5

total_time = time_needed + time_add

if current_record <= total_time:
    needed = total_time - current_record
    print(f"No, he failed! He was {needed:.2f} seconds slower.")

elif total_time < current_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
