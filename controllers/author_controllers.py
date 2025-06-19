from flask import Blueprint,jsonify
from models.author import Author

#Create the blueprint
author_bp=Blueprint('author_bp',__name__)

#Define the route
@author_bp.route('/author',methods=['GET'])
def get_author():
    authors= Author.query.all()
    response=[
        {
            'id':author.id,
            'name':author.name
        }
        for author in authors
    ]
    return jsonify(response),200