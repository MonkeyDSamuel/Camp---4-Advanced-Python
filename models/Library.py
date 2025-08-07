'''
    TASK:
        Create a librbary class 
            1. Instance variables: title, author, isbn. is_borrowed(boolean)
            2. Static variable or class variable:
                total_books(count of how many books were created in total)
            3. Local variable:
                Inside a method called borrow_book() use a local variable user_name that simulates the person borrowing the book.
            4. return_book changes the is_borrowed to false.
            5. Display or str method to display info

'''

class Library:
    'Class to manage Library books'
    total_books = 0
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False    #initial value is false
        # Library.total_books += 1    #book added or...
        Library.increment_books()

    @classmethod
    def increment_books(cls):
        cls.total_books += 1

    def borrow_book(self,user_name):
        if self.is_borrowed == False:
            self.is_borrowed = True
            return f"{user_name} is borrowing the book {self.title} by author,{self.author}."
        else:
            return f"Sorry!!{self.title} has already been borrowed by {user_name}"
    
    def return_book(self,user_name):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(f"{user_name} has returned the book, {self.title} successfully!!")
        else:
            print(f"Sorry!!! {user_name} don't have the book {self.title} in your possession to return...")
    
    def __str__(self):
        return f"Total Books: {Library.total_books} | Book Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Borrowed: {self.is_borrowed}"

bname = input("Enter the name of the book: ")
author = input("Enter the name of the book's author: ")
isbn = input("Enter the ISBN number: ")
user_name = input("Enter the name of the borrower/returner: ")

book1 = Library(bname,author,isbn)
print('\n')
print(book1.borrow_book(user_name))
print('\n')
print(book1.borrow_book("Samuel"))
book1.return_book(user_name)
print('\n')
print(book1)
