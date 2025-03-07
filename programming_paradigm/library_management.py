class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_checked_out(self):
        return self._is_checked_out
    
    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True
    
    def return_book(self):
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
            print(f"'{title}' not found in the library.")

    def return_book(self,title): 
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' is already available.")
                return
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")



    

        