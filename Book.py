import pandas as pd
from . import BookCategory

class Book:
    def __init__(self, title, author, category, subcategory, publish_date, num_edition, editor, available):

        created_category = BookCategory(category)
        subcategory = created_category.add_subcategory(subcategory)
        
        self.title = title
        self.author = author
        self.category = created_category
        self.subcategory = created_category.stringfy()
        self.publish_date = publish_date
        self.num_edition = num_edition
        self.editor = editor
        self.available = available
    
    def save(self, book):
        df = pd.read_csv('./persistance/books.csv')

        df = df.append(book, ignore_index=True)

        df.to_csv('./persistance/books.csv', index=False)
        return