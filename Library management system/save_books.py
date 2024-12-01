def save_all_books (all_books):
    with open("all_books.csv", "w") as fp:
        for book in all_books:
            line = f"{book ['title']} , {book['author']} , {book['year']} , {book['isbn']} , {book['quantity']} , {book['price']} \n"
            fp.write(line)
