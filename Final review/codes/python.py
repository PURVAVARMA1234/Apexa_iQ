class BankAccount:
    """
    A simple class to represent a bank account.

    Attributes:
        balance (int or float): The current monetary balance of the account.
    """
    def __init__(self, balance=0):
        """
        Initializes the BankAccount with a starting balance.

        Args:
            balance (int or float, optional): The initial balance. Defaults to 0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Adds a specified amount to the account balance.

        Args:
            amount (int or float): The amount to deposit.
        """
        self.balance += amount
        print(f"Deposited: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        """
        Subtracts a specified amount from the account balance,
        provided there is sufficient balance.

        Args:
            amount (int or float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Error: Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance: {self.balance}")

    def check_balance(self):
        """
        Prints the current account balance.
        """
        print(f"Balance: {self.balance}")


account = BankAccount(1000)
account.deposit(2000)
account.withdraw(200)
account.withdraw(2000)
account.check_balance()

###-------------------Library Management System-------------------###

class Book:
    """Represents a book with a title, author, and borrowing status."""
    def __init__(self, title, author):
        """Initializes a Book. Sets is_borrowed to False."""
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    """Represents a library member who can borrow and return books."""
    def __init__(self, name):
        """Initializes a Member with a name and an empty list of borrowed books."""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Allows the member to borrow a book if it's available."""
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        """Allows the member to return a borrowed book."""
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")

class Library:
    """Manages a collection of books."""
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self.books.append(book)

    def available_books(self):
        """Returns a list of titles for books that are not currently borrowed."""
        return [book.title for book in self.books if not book.is_borrowed]

    def borrowed_books(self):
        """Returns a list of titles for books that are currently borrowed."""
        return [book.title for book in self.books if book.is_borrowed]

library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("Python Programming", "John Doe")

library.add_book(book1)
library.add_book(book2)

member = Member("Alice")
member.borrow_book(book1)
print("Available books:", library.available_books())
member.return_book(book1)
print("Available books:", library.available_books())



# Fibonacci series up to n terms

def fibonacci(n):
    """
    Generates the first n numbers of the Fibonacci sequence.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


result = fibonacci(5)
print(result)


# Palindrome check
def is_palindrome(s):
    return s == s[::-1]
    """check whether the word follows palindrome or not"""

print("Palindrome check for 'radar':", is_palindrome("radar"))
print("Palindrome check for 'hello':", is_palindrome("hello"))


