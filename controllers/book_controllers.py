from flask import Blueprint,jsonify
from models.book import Book

#Create the blueprint
book_bp=Blueprint('book_bp',__name__)

#Define the route
@book_bp.route('/book',methods=['GET'])
def get_book():
    books= Book.query.all()
    response=[
        {
            'id':book.id,
            'name':book.name
        }
        for book in books
    ]
    return jsonify(response),200