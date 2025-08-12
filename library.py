from book import Book

class Library:
    def __init__(self):
        self.__books = list()
    
    def add_book(self, new_book):
        if not isinstance(new_book, Book):
            raise TypeError(f'Expected a "Book" object.')
        
        self.__books.append(new_book)
        return True
    
    def remove_book(self, title_book):
        if not title_book:
            raise ValueError('The title is empty.')
        
        elif not isinstance(title_book, Book):
            raise TypeError('Expected a "Book" object.')
        
        for book in self.__books:
            if book.get_title() == title_book:
                self.__books.remove(book)
                return True
    
    def list_books(self):
        if not self.__books:
            raise ValueError('No book available.')
        
        for book in self.__books:
            book.print_book()

    def lend_book(self, title_book):
        if not title_book:
            raise ValueError('The title is empty.')
        
        elif not isinstance(title_book, Book):
            raise TypeError('Excepted a "Book" object.')
        
        for book in self.__books:
            if book.get_title() == title_book:
                if book.get_availability == True:
                    book.get_availability = False
                    return True
                return False 

    def search_book(self, title_book):
        if not title_book:
            raise ValueError('The title is empty.')
        
        elif not isinstance(title_book, Book):
            raise TypeError('Excepted a "Book" object.')
        
        for book in self.__books:
            if book.get_title() == title_book:
                return True
            return False
