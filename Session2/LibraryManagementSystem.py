class Book:
    books = []
    
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True
        Book.books.append(self)
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")
    
    @classmethod
    def list_books(cls):
        if cls.books:
            print("\nList of Books:")
            for book in cls.books:
                status = "Available" if book.available else "Borrowed"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Status: {status}")
        else:
            print("No books available.")

# Menu-driven approach
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. List Books")
    print("5. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        ISBN = input("Enter book ISBN: ")
        Book(title, author, ISBN)
        print(f"Book '{title}' added successfully.")
    elif choice == "2":
        title = input("Enter book title to borrow: ")
        for book in Book.books:
            if book.title.lower() == title.lower():
                book.borrow_book()
                break
        else:
            print("Book not found.")
    elif choice == "3":
        title = input("Enter book title to return: ")
        for book in Book.books:
            if book.title.lower() == title.lower():
                book.return_book()
                break
        else:
            print("Book not found.")
    elif choice == "4":
        Book.list_books()
    elif choice == "5":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")