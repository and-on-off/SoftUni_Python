name_of_student = input()
grades_counter = 0
years_counter = 0
failed_counter = 0

while years_counter < 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_counter += 1
        if failed_counter > 1:
            excluded_year = years_counter + 1
            print(f"{name_of_student} has been excluded at {excluded_year} grade")
            break
        continue

    years_counter += 1
    grades_counter += annual_grade

else:
    average_grade = grades_counter / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
