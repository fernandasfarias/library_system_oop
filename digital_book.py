from book import Book
from random import uniform

class Digital_book(Book):
    def __init__(self, title:str, author:str, publication_year:int, availability:bool):
        super().__init__(title, author, publication_year, availability)
        self.__file_size = self.__get_size()
    
    def __get_size(self):
        return round(uniform(1.0, 40.0), 2)
    
    def print_digital_book(self):
        super().print_book()
        print(f'File size: {self.__file_size}')
