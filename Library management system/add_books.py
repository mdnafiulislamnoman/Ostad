from save_books import save_all_books

def add_books (all_books):
    title = input("Enter a book title:")
    author = input("Enter the author name:")
    isbn = int (input("Enter ISBN:"))
    year = int (input("Enter publishing year:"))
    price = int (input("Enter book price:"))
    quantity = int (input("Quantity of the book:"))

    book = {
        "title":title,
        "author":author,
        "year":year,
        "isbn":isbn,
        "quantity":year,
        "price":price,
    }
    all_books.append(book)
    save_all_books(all_books)

    print("Book added successfully.")

    return all_books