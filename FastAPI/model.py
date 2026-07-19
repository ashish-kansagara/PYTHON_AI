from pydantic import BaseModel

class librery(BaseModel):
    book_id  :  int
    book_name : str
    book_auther : str
    