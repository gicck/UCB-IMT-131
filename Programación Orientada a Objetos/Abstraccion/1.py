# =============================================================================
# EXAMPLE 1: WITHOUT OOP (Procedural Programming)
# =============================================================================

# Global variables to store data
books = []
borrowed_books = []

def add_book(title, author, isbn, copies):
    """Add a book to the library"""
    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'copies': copies,
        'available': copies
    }
    books.append(book)
    print(f"Added book: {title}")

def find_book_by_isbn(isbn):
    """Find a book by ISBN"""
    for book in books:
        if book['isbn'] == isbn:
            return book
    return None

def borrow_book(isbn, borrower_name):
    """Borrow a book"""
    book = find_book_by_isbn(isbn)
    if not book:
        print("Book not found!")
        return False
    
    if book['available'] <= 0:
        print("No copies available!")
        return False
    
    book['available'] -= 1
    borrowed_books.append({
        'isbn': isbn,
        'borrower': borrower_name,
        'title': book['title']
    })
    print(f"{borrower_name} borrowed '{book['title']}'")
    return True

def return_book(isbn, borrower_name):
    """Return a book"""
    book = find_book_by_isbn(isbn)
    if not book:
        print("Book not found!")
        return False
    
    # Find the borrowed record
    for i, borrowed in enumerate(borrowed_books):
        if borrowed['isbn'] == isbn and borrowed['borrower'] == borrower_name:
            book['available'] += 1
            borrowed_books.pop(i)
            print(f"{borrower_name} returned '{book['title']}'")
            return True
    
    print("No record of this book being borrowed by this person!")
    return False

def display_all_books():
    """Display all books in the library"""
    print("\n=== LIBRARY BOOKS ===")
    for book in books:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Available: {book['available']}/{book['copies']}")
        print("-" * 30)

# =============================================================================
# DEMONSTRATION CODE
# =============================================================================

def demo_without_oop():
    """Demonstrate the non-OOP approach"""
    print("=" * 50)
    print("DEMONSTRATION: WITHOUT OOP")
    print("=" * 50)
    
    # Add books
    add_book("Python Programming", "John Doe", "978-1111", 3)
    add_book("Data Structures", "Jane Smith", "978-2222", 2)
    
    # Display books
    display_all_books()
    
    # Borrow books
    borrow_book("978-1111", "Alice")
    borrow_book("978-1111", "Bob")
    
    # Display books after borrowing
    display_all_books()
    
    # Return a book
    return_book("978-1111", "Alice")
    display_all_books()


if __name__ == "__main__":
    # Run demonstrations
    demo_without_oop()