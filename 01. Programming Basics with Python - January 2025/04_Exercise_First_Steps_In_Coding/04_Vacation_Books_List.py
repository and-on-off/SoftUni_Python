book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

read_book = book_pages / pages_per_hour
hours_per_day = read_book / days

print(int(hours_per_day))
