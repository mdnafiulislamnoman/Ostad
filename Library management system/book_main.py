import add_books
import view_all_books

all_books = []

while True:
    print("Welcome to library management system.")
    print("Enter 0: to exit the program")
    print("Enter 1: to add a book")
    print("Enter 2: to view all books")

    menu = input("Enter any number:")

    if menu == "0":
        print("Thanks for using the system!!")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    else:
        print("Choose a valid number")
