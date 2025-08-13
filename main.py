from book import Book
from digital_book import Digital_book
from physical_book import Physical_book
from library import Library

welcome:str = '----------------- Welcome to a place where stories come to life -----------------\n'
print(welcome.center(100))
print('>>> This is a special place to register all your books!')
print('>>> You can add, remove an existing one, borrow and search for specific books!')

library = Library()
succeed = 0

while True:
    print('\n--- LIBRARY SYSTEM ---')
    print('1 - Exit\n2 - Add a Book\n3 - Remove a book\n4 - List all books\n5 - Borrow a Book\n6 - Search for a book\n')

    option = int(input('Type your option: '))

    if option == 1:
        succeed = 1
        break
    
    elif option == 2:
        type_book = int(input('Type "1" for physical book or "2" for digital book: '))
        
        while type_book != 1 and type_book != 2:
            type_book = int(input('Please, type a valid number. "1" for physical book or "2" for digital book: '))
        
        if type_book == 1:
            physical_read = Physical_book(None, None, 0, False, 0)
        else:
            digital_read = Digital_book(None, None, 0, False)

        # --- TITLE INPUT ---
        title = input('\nType the title of the book: ')
        
        successful_title = False
        limit_title = 0
        while not successful_title and limit_title < 5:
            try:
                if type_book == 1:
                    physical_read.set_title(title)
                else:
                    digital_read.set_title(title)
                
                successful_title = True
            
            except ValueError as e:
                print(f'ValueError: {e}')
                title = input('\nPlease, type the title of the book again: ')
                limit_title += 1
        
        if successful_title == False:
            break
        
        print('Title set successfully!')

        # --- AUTHOR INPUT ---
        author = input('\nEnter the author of the book: ')

        successful_author = False
        limit_author = 0

        while not successful_author and limit_author < 5:
            try:
                if type_book == 1:
                    physical_read.set_author(author)
                else:
                    digital_read.set_author(author)
                
                successful_author = True
            
            except ValueError as e:
                print(f'ValueError: {e}')
                author = input('\nPlease, enter a valid author: ')
                limit_author += 1
        
        if successful_author == False:
            break

        print('Author name set successfully!')

        # --- PUBLICATION YEAR SET ---
        year = int(input('\nEnter the publication year of the book: '))

        successful_year = False
        limit_year = 0
        while not successful_year and limit_year < 5:
            try:
                if type_book == 1:
                    physical_read.set_publication_year(year)
                else:
                    digital_read.set_publication_year(year)

                successful_year = True
            
            except ValueError as e:
                print(f'ValueError: {e}')
                year_str = int(input('\nPlease, enter a valid publication year: '))
                limit_year += 1
            
            except TypeError as e:
                print(f'TypeErro: {e}')
                year_str = int(input('\nPlease, enter a valid publication year: '))
                limit_year += 1
        
        if successful_year == False:
            break
        
        print('Publication year set successfully!')


if succeed == 0:
    print('\nYou exceeded the number of attempts. Please re-enter the system.')
else:
    print('\nThank you for using the library system! Come back as soon as possible!')