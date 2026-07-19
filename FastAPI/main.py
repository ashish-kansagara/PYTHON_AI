from fastapi import FastAPI,HTTPException
from model import librery
from typing import List

app=FastAPI()
books:List[librery]=[]

@app.get('/books',response_model=List[librery])
def get_book():
    return books

@app.get('/books/{book_id_fun}',response_model=librery)
def get_spe_book(book_id_fun:int):
    for index,book in enumerate(books):
        if book.book_id == book_id_fun:
            return books[index]
        
@app.post('/put_books',response_model=librery)
def put_book(new_book:librery):
    for index,book in enumerate(books):
        if new_book.book_id == book.book_id:
            raise HTTPException(status_code=400)
    books.append(new_book)
    return new_book
    
@app.put('/update_books/{book_id}',response_model=dict)
def updata_books(book_id:int,new_book:librery):
    for index,book in enumerate(books):
        if book.book_id == book_id:
            books[index]=new_book
    return {"message":"update succesfully"}
    
@app.delete('/del_book/{book_id}')
def del_book(book_id:int):
    for index,book in enumerate(books):
        if book.book_id == book_id:
            del books[index]
            return {"message":"delate succesfully"}
    raise HTTPException(status_code=400)
