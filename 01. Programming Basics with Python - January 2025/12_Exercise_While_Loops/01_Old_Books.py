book = input()
book_counter = 0

while True:
    guess_book = input()

    if guess_book == book:
        print(f"You checked {book_counter} books and found it.")
        book_counter += 1
        break

    elif guess_book != book:
        if guess_book == "No More Books":
            print(f"The book you search is not here!")
            print(f"You checked {book_counter} books.")
            break

        book_counter += 1
