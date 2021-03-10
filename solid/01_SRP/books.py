class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        searched_book = [book for book in self.books if book.title == title]
        if searched_book:
            return searched_book[0]
        return f"Book {title} not found"

    def add_book(self, book):
        self.books.append((book))


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Reader(Human):
    def __init__(self, name, surname, book):
        super().__init__(name, surname)
        self.book = book
        self.page = None

    def turn_page(self):
        if not self.page:
            self.page = 1
            return
        if self.page < self.book.pages:
            self.page += 1
            return
        return f"Book {self.book.title} is read"
