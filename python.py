class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance: {self.balance}")

    def check_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.check_balance()


###-------------------Library Management System-------------------###

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def available_books(self):
        return [book.title for book in self.books if not book.is_borrowed]

    def borrowed_books(self):
        return [book.title for book in self.books if book.is_borrowed]


# Example usage:
'''library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("Python Programming", "John Doe")

library.add_book(book1)
library.add_book(book2)

member = Member("Alice")
member.borrow_book(book1)
print("Available books:", library.available_books())
member.return_book(book1)
print("Available books:", library.available_books())'''

# Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("Fibonacci Series:", fibonacci(10))

# Pattern: Right-angled triangle
def pattern(n):
    for i in range(1, n + 1):
        print("* " * i)

print("Pattern:")
pattern(5)

# Palindrome check
def is_palindrome(s):
    return s == s[::-1]

print("Palindrome check for 'radar':", is_palindrome("radar"))
print("Palindrome check for 'hello':", is_palindrome("hello"))




