from User import User

class Book:
    def __init__ (self, title, isbn, author, genre, available, quantity):
        self.title = title
        self.isbn = isbn #int
        self.author = author
        self.genre = genre
        self.available = available #bool
        self.quantity = quantity #int

    def addBook(self):
        if self.title not in LibraryBooks:
            LibraryBooks[self.title] = self

        else:
            LibraryBooks[self.title].quantity = LibraryBooks[self.title].quantity + 1

    def borrowBook(user, book):

        if book not in LibraryBooks or LibraryBooks[book].available == False:
            print(f"\nSorry the book '{book}' isn't available!\n")
        else:
            
            User.setUserBooks(user, LibraryBooks[book], "add")
            print(f"\nSuccesfully added {book} to your account. Remember to bring it back!\n")
            if LibraryBooks[book].quantity > 1:
                LibraryBooks[book].quantity -= 1
            else:
                LibraryBooks[book].quantity -= 1
                LibraryBooks[book].available = False
            
        
    def returnBook(user, book):
        bookList = User.getUserBooks(user)
        if book not in bookList:
            print(f"Sorry, but user '{user}' hasn't borrowed book '{book}'")
        else:
            User.setUserBooks(user, LibraryBooks[book], "del")
            print(f"User '{user}' succesfully returned book '{book}'!")
            if LibraryBooks[book].quantity > 0:
                LibraryBooks[book].quantity += 1
            else:
                LibraryBooks[book].quantity += 1
                LibraryBooks[book].available = True

    def searchBook(title):
        book = LibraryBooks.get(title,"Sorry, book not found!")
        if book:
            print(f"Title: {book.title}, ISBN: {book.isbn}, Author: {book.author}, Genre: {book.genre}, Available: {book.available}, Quantity: {book.quantity}\n")
        

    def displayBooks():
        for book, details in LibraryBooks.items():
            print(f" - Title: {details.title}, ISBN: {details.isbn}, Author: {details.author}, Genre: {details.genre}, Available: {details.available}, Quantity: {details.quantity}\n")

LibraryBooks = {"1984": Book("1984", 124345436, "George Orwell", "Science Fiction", True, 2), "treasure island": Book("treasure island", 8049323, "Robert Louis Stevenson", "Fantasy", False, 0), "harry potter": Book("harry potter", 9872343245, "JK Rowling", "Fantasy", True, 10)}