# =============================================================================
# EXAMPLE 2: WITH OOP AND ABSTRACTION
# =============================================================================

class Book:
    """Represents a book in the library - demonstrates ABSTRACTION"""
    
    def __init__(self, title, author, isbn, copies):
        # These are the essential attributes that define a book
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = copies
        self.available_copies = copies
    
    def is_available(self):
        """Check if book is available for borrowing"""
        return self.available_copies > 0
    
    def borrow(self):
        """Borrow this book (decrease available copies)"""
        if self.is_available():
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        """Return this book (increase available copies)"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def get_info(self):
        """Get book information"""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'available': self.available_copies,
            'total': self.total_copies
        }
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author} (Available: {self.available_copies}/{self.total_copies})"

class BorrowRecord:
    """Represents a borrowing record - demonstrates ABSTRACTION"""
    
    def __init__(self, book, borrower_name):
        self.book = book
        self.borrower_name = borrower_name
        from datetime import datetime
        self.borrow_date = datetime.now()
    
    def get_record_info(self):
        """Get borrowing record information"""
        return {
            'book_title': self.book.title,
            'borrower': self.borrower_name,
            'borrow_date': self.borrow_date
        }

class Library:
    """Manages the entire library system - demonstrates ABSTRACTION"""
    
    def __init__(self, name):
        self.name = name
        self.books = {}  # isbn -> Book object
        self.borrow_records = []
    
    def add_book(self, title, author, isbn, copies):
        """Add a book to the library"""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists!")
            return False
        
        book = Book(title, author, isbn, copies)
        self.books[isbn] = book
        print(f"Added book: {title}")
        return True
    
    def find_book(self, isbn):
        """Find a book by ISBN"""
        return self.books.get(isbn)
    
    def borrow_book(self, isbn, borrower_name):
        """Process book borrowing"""
        book = self.find_book(isbn)
        if not book:
            print("Book not found!")
            return False
        
        if not book.is_available():
            print("No copies available!")
            return False
        
        if book.borrow():
            record = BorrowRecord(book, borrower_name)
            self.borrow_records.append(record)
            print(f"{borrower_name} borrowed '{book.title}'")
            return True
        
        return False
    
    def return_book(self, isbn, borrower_name):
        """Process book return"""
        book = self.find_book(isbn)
        if not book:
            print("Book not found!")
            return False
        
        # Find the borrow record
        for i, record in enumerate(self.borrow_records):
            if (record.book.isbn == isbn and 
                record.borrower_name == borrower_name):
                
                book.return_book()
                self.borrow_records.pop(i)
                print(f"{borrower_name} returned '{book.title}'")
                return True
        
        print("No record of this book being borrowed by this person!")
        return False
    
    def display_all_books(self):
        """Display all books in the library"""
        print(f"\n=== {self.name.upper()} BOOKS ===")
        for book in self.books.values():
            print(book)
            print("-" * 40)
    
    def get_borrowed_books(self):
        """Get list of currently borrowed books"""
        return [record.get_record_info() for record in self.borrow_records]
    
def demo_with_oop():
    """Demonstrate the OOP approach with abstraction"""
    print("\n" + "=" * 50)
    print("DEMONSTRATION: WITH OOP AND ABSTRACTION")
    print("=" * 50)
    
    # Create a library
    library = Library("University Library")
    
    # Add books
    library.add_book("Python Programming", "John Doe", "978-1111", 3)
    library.add_book("Data Structures", "Jane Smith", "978-2222", 2)
    
    # Display books
    library.display_all_books()
    
    # Borrow books
    library.borrow_book("978-1111", "Alice")
    library.borrow_book("978-1111", "Bob")
    
    # Display books after borrowing
    library.display_all_books()
    
    # Return a book
    library.return_book("978-1111", "Alice")
    library.display_all_books()

if __name__ == "__main__":
    demo_with_oop()
