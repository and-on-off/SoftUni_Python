people_count = int(input())
nights = int(input())
travel_cards = int(input())
tickets = int(input())

total_nights_per_one = nights * 20
total_travel_cards_per_one = travel_cards * 1.60
total_tickets = tickets * 6

total_one_person = total_nights_per_one + total_travel_cards_per_one + total_tickets
total_group = total_one_person * people_count

final_sum = total_group * 1.25

print(f"{final_sum:.2f}")