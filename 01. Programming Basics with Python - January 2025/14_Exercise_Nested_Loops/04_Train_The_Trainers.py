judge_count = int(input())

presentation_name = input()
total_score = 0
total_presentations = 0

while presentation_name != 'Finish':
    total_presentations += judge_count
    current_score = 0

    for score in range(judge_count):
        current_score += float(input())

    total_score += current_score
    print(f'{presentation_name} - {current_score / judge_count:.2f}.')

    presentation_name = input()

print(f"Student's final assessment is {total_score / total_presentations:.2f}.")