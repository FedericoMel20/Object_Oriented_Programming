import json

file = 'books.json'

try:
    with open(file, "r") as f:
        books = json.load(f)
        print(books)
except:
    books = []

def save_toJson():
    with open("books.json", "w") as data:
        json.dump(books,data)


def add_book():
    title = input("Insert book Title: ")
    author = input("Insert book Author: ")
    year = input("Insert book year: ")
    genre = input("Insert book genre: ")
    borrowed = input("Is the book borrowed: ")

    book = {
        'title' : title,
        'author' : author,
        'year' : year,
        'genre' : genre,
        'borrowed' : borrowed,
    }

    books.append(book)
    list_book()
    save_toJson()

def list_book():
    for index, book in enumerate(books):
        print("No: ", index+1)
        print('Title: ', book['title'])
        print('Author: ', book['author'])  
        print('Year: ', book['year']) 
        print('Genre: ', book['genre'])
        print('Borrowed: ', book['borrowed'])
        print("------------")

def edit_book():
    no_book = int(input("Choose number of the book you want to edit: "))
    new_book = books[no_book -1]
    print("Current Details: ")
    print('1. Title: ', new_book['title'])
    print('2. Author: ', new_book['author'])  
    print('3. Year: ', new_book['year']) 
    print('4. Genre: ', new_book['genre'])
    print('5. Borrowed: ', new_book['borrowed'])

    update_book = input("Choose which one you want to update: ")
    if(update_book == "1"):
        new_book['title'] = input('Input new Title: ')
    elif(update_book == "2"):
        new_book['author'] = input('Input new author: ') 
    elif(update_book == "3"):
        new_book['year'] = input('Input new year: ')
    elif(update_book == "4"):
        new_book['genre'] = input('Input new genre: ')
    else:
        print("No option")
    books[no_book-1] = new_book
    save_toJson()
    



def delete_book():
    no_book = input("Choose number of the book you want to delete: ")
    books.pop(int(no_book) -1)
    print("Book successfully deleted")
    save_toJson()

while True:
    print("--Please Choose Menu--")
    print("1. Add Book")
    print("2. List of Books")
    print("3. Edit Book")
    print("4. Delete Book")
    print("5. Exit")

    menu = input("Choose a number from the menu: ")
    if(menu == "1"):
        add_book()
    elif(menu == "2"):
        list_book()
    elif(menu == "3"):
        edit_book()
    elif(menu == "4"):
        delete_book()
    elif(menu == "5"):
        break
    else:
        print("Invalid menu")

