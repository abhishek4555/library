library = []

def add_book():
    book = input("Enter book name: ")
    author = input("Enter author name: ")

    library.append({
        "book": book,
        "author": author,
        "issued": False
    })

    print("Book added successfully!")

def view_books():
    if len(library) == 0:
        print("No books available.")
        return

    print("\nLibrary Books:")
    for i, book in enumerate(library, start=1):
        status = "Issued" if book["issued"] else "Available"
        print(f"{i}. {book['book']} - {book['author']} ({status})")

def issue_book():
    view_books()
    if len(library) == 0:
        return

    num = int(input("Enter book number to issue: "))

    if 1 <= num <= len(library):
        if library[num-1]["issued"]:
            print("Book is already issued.")
        else:
            library[num-1]["issued"] = True
            print("Book issued successfully!")
    else:
        print("Invalid book number.")

def return_book():
    view_books()
    if len(library) == 0:
        return

    num = int(input("Enter book number to return: "))

    if 1 <= num <= len(library):
        if library[num-1]["issued"]:
            library[num-1]["issued"] = False
            print("Book returned successfully!")
        else:
            print("Book was not issued.")
    else:
        print("Invalid book number.")

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.")