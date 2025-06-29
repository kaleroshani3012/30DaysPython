from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class book(BaseModel):

    id: int
    title : str
    author : str
    year : int

books_db: List[book] = []


@app.get("/")
def home():
    return {"message": "Welcome to the Library API"}

#this function is to get all book
@app.get("/books", response_model = List[book])
def get_books():
    return books_db

#this function is to get single book by id
@app.get("/books/{book_id}",response_model = book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    
    raise HTTPException(status_code = 404, detail="Book not Found")

#this function is to add new book into books_db
@app.post("/books", response_model = book)
def add_book(Book: book):
    for b in books_db:
        if isinstance(b, book) and b.id == Book.id:
            raise HTTPException(status_code = 400, detail = "Book with this ID is already Available")
    books_db.append(Book)
    return Book

#now this fuunction is for update an existing book
@app.put("/books/{book_id}", response_model = book)
def update_book(book_id: int, updated_book: book):
    for index, book in enumerate(books_db):
        if book_id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not Found")

#this function is for delating book from books_db
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return {"message": f"Book with ID {book_id} deleted succesfully :)"}
    raise HTTPException(status_code=404, detail="Book not Found")