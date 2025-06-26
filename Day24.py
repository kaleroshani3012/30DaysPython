from dataclasses import dataclass
from typing import List

@dataclass
class LibraryBook:

    title: str
    author: str
    isbn: str
    publish_year: int
    available: bool = True


    def display(self):
        status = "Available ✅" if self.available else "Not Available ❌"
        print(f"'{self.title}' by {self.author} | ISBN: {self.isbn} | {status} ")

lib: List[LibraryBook] = []

def add_book():
    print("\nAdd New Book:\n ")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    year = int(input("Publication Year: "))

    book = LibraryBook(title, author, isbn, year)
    lib.append(book)
    print(f"{title} book added succesfully\n")

def view_books(avail=False):
    print("\n Library Books: \n")
    found = False
    for book in lib:
        if not avail or book.available:
            book.display()
            found = True
        if not found:
            print("No Book Found.\n")

def borrow_book():
    title = input("Enter Title of the book to borrow: ")
    for book in lib:
        if book.title.lower() == title.lower():
            if book.available:
                book.available= False
                print(f"\nYou Borrowed {book.title} Book by author {book.author}.\n")
            else:
                print(f"\n'{book.title}' book is already Borrowed\n ")
            return 
    print("oops, Book Not Found")

def return_book():
    title = input("Enter Title of the book to return: ")
    for book in lib:
        if book.title.lower() == title.lower():
            if not book.available:
                book.available = True
                print(f"'{book.title}' book by author {book.author} Returned Sucessfully\n")
            else:
                print(f"'{book.title}' by author {book.author} was not Borrowed\n ")
            return
    print("oops, Book Not Found")

def main():
    name = input("Enter Your Name: ").capitalize()
    while True:
        print(f"\nHey {name} Welcome to Krishna Libary\n")
        print("1. Add Book")
        print("2. View All Books")
        print("3. View Available Books")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Exit")
     
        ch = input(f"\n{name} Please Enter from option 1 to 6 to Proceed: ")

        if ch == '1':
            add_book()
        elif ch == '2':
            view_books()
        elif ch == '3':
            view_books(avail=True)
        elif ch == '4':
            borrow_book()
        elif ch == '5':
            return_book()
        elif ch == '6':
            print(f"\nHey {name} Exiting from System, Welcome Back Again!!!\n")
            break
        else:
            print(f"\noops {name},  Invalid Choice \n Please Select from 1 to 6 ")

if __name__ == '__main__':
    main()

