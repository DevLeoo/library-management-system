class BookCategory:
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def add_subcategory(self, category):
        self.subcategories.append(category)

    def remove_subcategory(self, category):
        self.subcategories.remove(category)

    
    def stringify(self):
        return str(self.subcategories)