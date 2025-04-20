library_catalogue = {
    "1984": {"Author": "George Orwell", "Publication Year": 1949},
    "To Kill a Mockingbird": {"Author": "Harper Lee", "Publication Year": 1960},
    "The Great Gatsby": {"Author": "F. Scott Fitzgerald", "Publication Year": 1925},
    "Moby Dick": {"Author": "Herman Melville", "Publication Year": 1851}
}

library_catalogue["Pride and Prejudice"] = {"Author": "Jane Austen", "Publication Year": 1813}

book_title = "1984"
if book_title in library_catalogue:
    print(f"Book Found: {book_title}")
    print("Details:", library_catalogue[book_title])
else:
    print("Book not found in the catalogue.")