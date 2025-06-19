from flask import Blueprint,jsonify
from models.genre import Genre

#Create the blueprint
genre_bp=Blueprint('genre_bp',__name__)

#Define the route
@genre_bp.route('/genre',methods=['GET'])
def get_genre():
    genres=Genre.query.all()
    response=[
        {
            'id':genre.id,
            'name':genre.name
        }
        for genre in genres
    ]
    return jsonify(response),200