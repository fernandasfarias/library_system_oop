from book import Book

class Physical_book(Book):
    def __init__(self, title:str, author:str, publication_year:int, availability:bool, pages:int):
        super().__init__(title, author, publication_year, availability)
        self.__pages = pages
    
    def get_pages(self):
        return self.__pages
    
    def set_pages(self, new_number_pages):
        if not new_number_pages:
            raise ValueError('The number of pages is not specified.')
    
        elif not new_number_pages.isdigit():
            raise TypeError('The number of pages is not an integer.')
        
        self.__pages = int(new_number_pages)
        return True
    
    def print_physical_book(self):
        super().print_book()
        print(f"Number of pages: {self.__pages}")
