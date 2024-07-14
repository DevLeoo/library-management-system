class ReturnManager:
    def return_book(self, book):
        book.available = True
        return f"{book.title} foi devolvido com sucesso."