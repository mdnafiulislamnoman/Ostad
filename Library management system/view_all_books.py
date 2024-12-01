def view_all_books (all_books):
    if all_books != []:
        for book in all_books:
            print(f"{book ['title']} , {book['author']} , {book['year']} , {book['isbn']} , {book['quantity']} , {book['price']} \n")
    else:
        print("No book found in program")