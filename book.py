from random import randint

class Book:
    def __init__(self, title:str, author:str, publication_year:int, availability:bool):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__availability = availability
        self.__code = self.__generate_code() # private method
    
    def __generate_code(self):
        self.__code = randint(1, 500)
    
    # --- GETTER METHODS ---
        # Remember that, usually, the get method doesn't need exception handling.
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publication_year(self):
        return self.__publication_year
    
    def get_availability(self):
        return self.__disponibility
    
    # --- SETTER METHODS --- 
    
    # in this case, I need to check if the title is not empty or if the type is not a string(exception handling)
    def set_title(self, new_title):
        if not new_title:
            raise ValueError('The title is empty.')
        
        self.__title = new_title
        return True

    # the same thing happens with the set of authors
    def set_author(self, new_author):
        if not new_author:
            raise ValueError('The author is empty.')
        
        self.__author = new_author
        return True

    # in this case, I need to check if the year is a positive integer
    def set_publication_year(self, new_publication_year):
        if not new_publication_year:
            raise ValueError('The publication year is empty.')

        elif new_publication_year <= 0:
            raise ValueError('The publication year must be a positive integer.')

        elif not isinstance(new_publication_year, int):
            raise TypeError('The publication year must be a positive integer.')

        self.__publication_year = new_publication_year
        return True
    
    # I need to check if availability is a boolean value
    def set_availability(self, new_availability):
        if not new_availability:
            raise ValueError('The availability is empty.')
        
        elif not isinstance(new_availability, bool):
            raise TypeError('The availability must be a boolean value (True or False).')
        
        self.__availability = new_availability
        return True

    # --- PRINT ---
    def print_book(self):
        print(f'Title: {self.__title}')
        print(f'Author: {self.__author}')
        print(f'Publication year: {self.__publication_year}')
        print(f'Availability: {self.__availability}')
        print(f'Code: {self.__code}')
    