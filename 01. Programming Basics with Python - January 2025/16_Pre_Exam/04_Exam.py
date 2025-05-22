students = int(input())
group1 = 0
group2 = 0
group3 = 0
failed = 0
sum_grades = 0
average = 0


for student in range(1, students + 1):
    grade = float(input())

    if grade >= 5:
        group1 += 1
    elif 4.00 <= grade < 5:
        group2 += 1
    elif 3.00 <= grade < 4:
        group3 += 1
    elif grade < 3:
        failed += 1
    sum_grades += grade


average = sum_grades / students
group1 = group1 / students * 100
group2 = group2 / students * 100
group3 = group3 / students * 100
failed = failed / students * 100



print(f"Top students: {group1:.2f}%")
print(f"Between 4.00 and 4.99: {group2:.2f}%")
print(f"Between 3.00 and 3.99: {group3:.2f}%")
print(f"Fail: {failed:.2f}%")
print(f"Average: {average:.2f}")