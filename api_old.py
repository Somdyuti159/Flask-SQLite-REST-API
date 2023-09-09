## In memory storage, not database used

from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return 'Hello World!'

'''
Examples:
A standard CRUD Books API

GET request to /api/books returns the details of all the books
POST request to /api/books creates a book with the ID 3(As per request body)

Sample request body
{
    "id": "1",
    "name": "A Game of Thrones",
    "author": "George R R Martin"
}
GET request to /api/books/3 reutrns the details of book 3
PUT request to /api/books/3 to update fields of book 3
DELETE request to /api/books/3 deletes book 3

'''

books= {
    '1':{
        "id": "1",
        "name": "A Game of Thrones",
        "author": "George R. R. Martin"
    },
    '2':{
        "id": "2",
        "name": "Lord of the Rings",
        "author": "J. R. R. Tolkein"
    }
}


@app.route('/api/books', methods =['GET', 'POST'])
def api_books():
    if request.method == "GET":
        return make_response(jsonify(books),200)
    
    elif request.method == "POST":
        content = request.json
        book_id = content['id']
        books[book_id] = content

        book_obj = books.get(book_id, {})
        return make_response(jsonify(book_obj),201) #201=Created
    
@app.route('/api/books/<book_id>', methods =['GET','PUT','DELETE'])
def api_each_books(book_id):
    if request.method == "GET":
        book_obj=books.get(book_id,{})
        if book_obj:
            return make_response(jsonify(book_obj),200)
        else:
            return make_response(jsonify(book_obj),404)
    
    elif request.method == "PUT":  #Updates the request
        content = request.json
        books[book_id] = content

        book_obj = books.get(book_id, {})
        return make_response(jsonify(book_obj),200)    
    
    elif request.method == "DELETE":
        if book_id in books:
            del(books[book_id])
        
        return make_response(jsonify({}),204)


if __name__ == '__main__':
    app.run(debug=True)