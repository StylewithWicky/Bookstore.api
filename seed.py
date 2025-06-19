from app import create_app
from models import db
from models.author import Author
from models.genre import Genre
from models.book import Book

app = create_app()

def seed_data():
    with app.app_context():
        print("📦 Seeding data...")

        # Clear existing data
        Book.query.delete()
        Author.query.delete()
        Genre.query.delete()

        # Create genres
        fiction = Genre(name="Fiction")
        nonfiction = Genre(name="Non-Fiction")
        fantasy = Genre(name="Fantasy")

        db.session.add_all([fiction, nonfiction, fantasy])
        db.session.commit()
        print("✅ Genres added")

        # Create authors
        rowling = Author(name="J.K. Rowling")
        orwell = Author(name="George Orwell")
        angelou = Author(name="Maya Angelou")

        db.session.add_all([rowling, orwell, angelou])
        db.session.commit()
        print("✅ Authors added")

        # Create books
        book1 = Book(
            title="Harry Potter and the Sorcerer's Stone",
            description="A young wizard's journey begins.",
            author=rowling, genre=fantasy
        )
        book2 = Book(
            title="1984",
            description="Dystopian society under surveillance.",
            author=orwell, genre=fiction
        )
        book3 = Book(
            title="I Know Why the Caged Bird Sings",
            description="Memoir of Maya Angelou.",
            author=angelou, genre=nonfiction
        )

        db.session.add_all([book1, book2, book3])
        db.session.commit()
        print("✅ Books added\n🎉 Done seeding!")

if __name__ == "__main__":
    seed_data()
