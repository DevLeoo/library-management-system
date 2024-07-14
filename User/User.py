import pandas as pd

class User:
    def __init__(self, name, user_type):
        self.name = name
        self.type = user_type # 1 - Student 2 - Staff 3 - Teacher 
        self.max_loans = 2
        self.current_loans = 0

    def perform_operation(self):
        raise NotImplementedError("No permission")
    
    def update(self, message):
        print(f"{self.name} received notification: {message}")


    def is_eligible(self):
        pass

    def save(self, book):
        df = pd.read_csv('./persistance/users.csv')

        df = df.append(book, ignore_index=True)

        df.to_csv('./persistance/users.csv', index=False)
        return