import LoanLimitHandler
import UserEligibilityHandler
import BookAvailabilityHandler

class LoanManager:

    def __init__(self, book, user):
        self.book = book
        self.user = user
        self.approved = False


    def loan_book(self):
        loan_limit_handler = LoanLimitHandler()
        user_eligibility_handler = UserEligibilityHandler(loan_limit_handler)
        book_availability_handler = BookAvailabilityHandler(user_eligibility_handler)

        result = book_availability_handler.handle(self)
        if result is True:
            self.approved = True
            self.user.current_loans += 1  
            print(f"Loan approved - {self.book.title}.")
        else:
            print(f"Loan denied: {result}")