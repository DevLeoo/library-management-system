class BookAvailabilityNotifier:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def new_book_added(self, book):
        message = f"New book added: {book}"
        self.notify(message)

