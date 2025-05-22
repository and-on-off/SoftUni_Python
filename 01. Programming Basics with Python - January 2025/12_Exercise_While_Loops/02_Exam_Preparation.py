failed_threshold = int(input())
failed_times = 0
number_of_problems = 0
average_score = 0
last_problem = ""
has_failed = ""

while failed_times < failed_threshold:
    problem_name = input()

    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        has_failed = True
        failed_times += 1

    average_score += grade
    number_of_problems += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f"Average score: {average_score / number_of_problems:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
