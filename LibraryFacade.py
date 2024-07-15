import Library
import Loan as LoanManager
import Return as ReturnManager
import Book

class LibraryFacade:
    def __init__(self):
        self.library = Library()
        self.loan_manager = LoanManager()
        self.return_manager = ReturnManager()

    def add_book(self, title, author):
        book = Book(title, author)
        self.library.add_book(book)

    def save_lib(self):
        self.library.save()

    def find_book(self, title):
        return self.library.find_book(title)

    def loan_book(self, title, user):
        book = self.library.find_book(title)
        if book:
            loan = LoanManager(book, user)
            return loan.loan_book()
        print("Book not found")
        return

    def return_book(self, title):
        book = self.library.find_book(title)
        if book:
            return self.return_manager.return_book(book)
        print("Book not found")
        return


"""
if __name__ == "__main__":
    facade = LibraryFacade()

    # Adicionando livros à biblioteca
    facade.add_book("1984", "George Orwell")
    facade.add_book("Brave New World", "Aldous Huxley")

    # Buscando um livro
    print(facade.find_book("1984").title)  # Saída: 1984

    # Emprestando um livro
    print(facade.loan_book("1984"))  # Saída: 1984 foi emprestado com sucesso.

    # Tentando emprestar novamente
    print(facade.loan_book("1984"))  # Saída: Livro não encontrado.

    # Devolvendo um livro
    print(facade.return_book("1984"))  # Saída: 1984 foi devolvido com sucesso.

"""