from flask import Flask, request, jsonify
import pandas as pd
from . import Book
from . import LibraryFacade
from User import User
from . import BookAvailabilityNotifier

app = Flask(__name__)

@app.route('/api/book', methods=['GET'])
def get_data():
    df = pd.read_csv("./persistance/books.csv")
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/book/register', methods=['POST'])
def register_book():
    jhon = User("John", 3)
    doe = User("Doe", 1)

    notifier = BookAvailabilityNotifier()
    notifier.subscribe(jhon)
    notifier.subscribe(doe)

    data = request.json
    data["available"] = True

    book = Book(
        data['title'],
        data['author'], 
        data['category'],
        data['subcategory'],
        data['publish_date'],
        data['num_edition'],
        data['editor'],
        data["available"] or True
    )

    lib_facade = LibraryFacade()
    lib_facade.add_book(book)
    lib_facade.persist_book(book)
    lib_facade.persist_lib()

    notifier.new_book_added(book['title'])

    return jsonify({"name": "successfuly registered"}), 201


@app.route('/api/book/loan', methods=['POST'])
def rent_book():
    # data = {"title": "1984"}
    data = request.json
    user = User("John Doe", 1)

    lib_facade = LibraryFacade()
    lib_facade.loan_book(data["title"], user)
    
    return jsonify({"name": "successfuly rented"}), 201

@app.route('/api/book/return', methods=['POST'])
def rent_book():
    # data = {"title": "1984"}
    data = request.json
    
    lib_facade = LibraryFacade()
    lib_facade.return_book(data['title'])

    return jsonify({"name": "successfuly returned"}), 201



if __name__ == '__main__':
    app.run(debug=True, port=3000)
