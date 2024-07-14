import pandas as pd

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                return book
        return None
    
    def save(self,):
        df = pd.read_csv('./persistance/library.csv')

        for book in self.books:
            df = df.append(book, ignore_index=True)

        df.to_csv('./persistance/library.csv', index=False)
        return