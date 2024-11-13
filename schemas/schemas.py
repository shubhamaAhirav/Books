from pydantic import BaseModel
from typing import List, Optional

class AuthorSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class BookSchema(BaseModel):
    id: int
    title: str
    language: str
    genre: str
    subjects: Optional[str]
    bookshelves: Optional[str]
    downloads: int
    mime_type: Optional[str]
    author: AuthorSchema

    class Config:
        orm_mode = True
