from . import Book

class ExternalCatalogAdapter:
    def __init__(self, external_catalog):
        self.external_catalog = external_catalog

    def get_books(self):
        external_data = self.external_catalog.fetch_book_data()
        books = [Book(
            data['title'],
            data['author'], 
            data['category'],
            data['subcategory'],
            data['publish_date'],
            data['num_edition'],
            data['editor'],
            data['available']
        ) for data in external_data]
        return books
    
"""
external_catalog = ExternalCatalog()
    
    # Usando o adapter
    adapter = ExternalCatalogAdapter(external_catalog)
    books = adapter.get_books()

    # Exibindo os livros
    for book in books:
"""