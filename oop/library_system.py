# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition class: Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_info())


