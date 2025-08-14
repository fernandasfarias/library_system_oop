from book import Book

class Library:
    def __init__(self):
        self.__books = list()
    
    def add_book(self, new_book):        
        self.__books.append(new_book)
        return True
    
    def remove_book(self, title_book):
        for book in self.__books:
            if book.get_title() == title_book:
                self.__books.remove(book)
                return True
        return False

    def list_books(self):
        for book in self.__books:
            book.print_book()
        return True

    def lend_book(self, title_book):        
        for book in self.__books:
            if book.get_title() == title_book:
                if book.get_availability() == True:
                    book.set_availability('False')
                    return True
        return False

    def search_book(self, title_book):   
        for book in self.__books:
            if book.get_title() == title_book:
                return True
        return False