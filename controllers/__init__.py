from .author_controllers import author_bp
from .book_controllers import book_bp
from .genre_controllers import genre_bp

def register_routes(app):
    app.register_blueprint(author_bp)
    app.register_blueprint(genre_bp)
    app.register_blueprint(book_bp)