# Project Requirements

# In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System. 
# This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a 
# robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.

# Enhanced User Interface (UI) and Menu:

#     Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.

#     Welcome to the Library Management System!

#     Main Menu:
#     1. Book Operations
#     2. User Operations
#     3. Author Operations
#     4. Genre Operations
#     5. Quit

#         Book Operations:

#         Book Operations:
#         1. Add a new book
#         2. Borrow a book
#         3. Return a book
#         4. Search for a book
#         5. Display all books

#         User Operations:

#         User Operations:
#         1. Add a new user
#         2. View user details
#         3. Display all users

#         Author Operations:

#         Author Operations:
#         1. Add a new author
#         2. View author details
#         3. Display all authors

#         Genre Operations:

#         Genre Operations:
#         1. Add a new genre
#         2. View genre details
#         3. Display all genres

# Class Structure:

#     Implement a class structure that represents key entities in the library management system, including:
#         Book: A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
#         User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
#         Author: A class representing book authors with attributes like name and biography.
#         Genre: A class representing book genres with attributes like name, description, and category.

# Encapsulation:

#     Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.

# Inheritance and Polymorphism:

#     Utilize inheritance to create specialized book categories (e.g., Fiction, Non-fiction, Mystery) that inherit common properties and methods from the base Book class. 
# Overload methods as needed in the subclasses. For example, in a subclass FictionBook, you can override the __str__ method to include additional information specific to fiction books.

# Modules:

#     Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.

# Menu Actions:

#     Implement the following actions in response to menu selections using the classes you've created:

# - Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as "Borrowed."
# - Allowing users to return a book, marking it as "Available."
# - Searching for a book by its unique identifier (ISBN or title) and displaying its details.
# - Displaying a list of all books with their unique identifiers.
# - Adding a new user with user details.
# - Viewing user details.
# - Displaying a list of all users.
# - Adding a new author with author details.
# - Viewing author details.
# - Displaying a list of all authors.
# - Adding a new genre with genre details.
# - Viewing genre details.
# - Displaying a list of all genres.
# - Quitting the application.

# User Interaction:

#     Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
#     Implement input validation using regular expressions (regex) to ensure the correct formatting of user input.

# Error Handling:

#     Implement error handling using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

# GitHub Repository:

#     Create a GitHub repository for your project and commit code regularly.
#     Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
#     Include a link to your GitHub repository in your project documentation.

# Optional Bonus Points

#     Text File Handling (Bonus): Implement text file handling to load and save data for various entities in the library management system, such as books, users, authors, and genres. 
# Create dedicated text files for each entity type and develop methods to read data from these files during system startup and save data to them when changes occur. Ensure data integrity
#     and error handling during file operations.
#     Reservation System (Bonus): Enhance the system by implementing a reservation system. Users can reserve books that are currently unavailable, and the system will notify them when 
# the book becomes available. Develop methods to handle reservations, check availability, and notify users of reservation status changes.
#     Fine Calculation (Bonus): Implement a fine calculation system for overdue books. Assign due dates to borrowed books, and calculate fines for users who exceed the due date. 
# Develop a mechanism for users to pay fines and update their accounts accordingly.

# Submission

#     Upon completing the project, submit your code, including all source code files, and the README.md file in your GitHub repository to your instructor or designated platform.

# Project Tips

#     Begin by designing a class hierarchy that represents the library's structure and entities.
#     Test your code iteratively as you implement each feature to identify and address any potential bugs or issues.
#     Collaborate with peers, seek assistance, and remember that learning is a collaborative effort.

# Conclusion

# By successfully completing this project, you will not only enhance your Python programming skills but also create a sophisticated Library Management System that demonstrates your 
# mastery of Object-Oriented Programming principles and effective code organization. Get ready to build a digital haven for book enthusiasts and embark on this exciting coding journey!
from Book import Book
from Author import Author
from Genre import Genre
from User import User

print("Welcome to the library system!\n")
username = input("Please input username:\n").strip().lower().title()
User.addUser(username)

while True:
    print("\nWhat menu would you like to navigate to?\n")
    action = input("Choose between: Book, User, Author, Genre - or enter Quit to exit the program\n").strip().lower()
    
    if action == "book":
        print("Great, lets pull up the 'Book' menu...\n\n")
        print("What 'Book' related action would you like to take?\n")
        choice = input("Choose from the following: Add new, Borrow, Return, Search, Display all - or 'exit' to return to the previous menu\n").strip().lower()
        
        if choice == "add new":
            print("\nOk lets add a new book!\n")
            title = input("What is the title of your book?\n").strip().lower().title()
            isbn = input("What is the isbn of your book?\n").strip()
            author = input("Who is the author of your book?\n").strip().lower().title()
            Author.addAuthor(author)
            print("\n")
            Genre.displayAllGenres()
            genre = input("\nWhich is the genre of your book? select from the list or enter 'new' to create new genre\n").strip().lower().title()
            Genre.addNew(genre)
            Book.addBook(Book(title, isbn, author, genre, True, 1))
            print(f"\n Your new book titled '{title}' of the '{genre}' Genre has been added to the Library!\n")

        elif choice == "borrow":
            print("\nOk lets borrow a book for you...\n")
            Book.displayBooks()
            book = str(input("\nWhich book would you like to borrow?\n").strip().lower().title())
            Book.borrowBook(username, book)

        elif choice == "return":
            print("\nOk lets return a book for you...\n")
            bookList = User.getUserBooks(username)
            print("Here's a list of your books:")
            for book in bookList:
                print(book)
            book = str(input("\nWhich book would you like to return?").strip().lower().title())
            Book.returnBook(username, book)

        elif choice == "search":
            print("\nOk, lets search for a book...\n")
            book = input("Enter the book title:\n").strip().lower().title()
            Book.searchBook(book)
            
        elif choice == "display all":
            print("\nOk, lets take a look at all the books in the system...\n")
            Book.displayBooks()

        elif choice == "exit":
            print("\nReturning to previous menu...\n")
            continue
        else:
            print("\nReturning to previous menu...\n")
            continue


    if action == "user":
        print("Great, lets pull up the 'User' menu...\n\n")
        print("What 'User' related action would you like to take?\n")
        choice = input("Choose from the following: Add new, User details, Display all, or 'exit' to return to the previous menu\n").strip().lower()
        
        if choice == "add new":
            print("\nOk lets add a new user...")
            name = input("\nWhats the name of your new user:\n").lower().title()
            User.addUser(name)
            
        elif choice == "user details":
            print("\nOk lets check out some user details...")
            name = input("\nWhats the name of the user you want to know about?\n").lower().title()
            User.getUserDetails(name)
            
        elif choice == "display all":
            User.displayAllUsers()
            
        elif choice == "exit":
            print("\nReturning to previous menu...\n")
            continue
        else:
            print("\nReturning to previous menu...\n")
            continue

    if action == "author":
        print("Great, lets pull up the 'Author' menu...\n\n")
        print("What 'Author' related action would you like to take?\n")
        choice = input("Choose from the following: Add new, Author details, Display all, or 'exit' to return to the previous menu\n").strip().lower()
        
        if choice == "add new":
            print("\nOk, lets add a new author...\n")
            name = input("Please enter the name of the author you'd like to add...\n").strip().lower().title()
            Author.addAuthor(name)
            
        elif choice == "author details":
            print("\nOk, lets pull up our list of authors:\n")
            Author.displayAllAuthors()
            name = input("\nPlease enter the name of the author you'd like to check out... (case sensitive)\n").strip().lower().title()
            Author.getAuthorDetails(name)

        elif choice == "display all":
            print("\nOk, lets pull check out all the authors we have in the database..\n")
            Author.displayAllAuthors()

        elif choice == "exit":

            print("\nReturning to previous menu...\n")
            continue
        else:
            print("\nReturning to previous menu...\n")
            continue

    if action == "genre":
        print("Great, lets pull up the 'Genre' menu...\n\n")
        print("What 'Genre' related action would you like to take?\n")

        choice = input("Choose from the following: Add new, Genre details, Display all, Books of genre, or 'exit' to return to the previous menu\n").strip().lower()
        if choice == "add new":
            print("\nOk, lets add a new genre..\n")
            name = input("What's the name of the genre you'd like to add?").strip().lower().title()
            Genre.addNew(name)
            
        elif choice == "genre details":
            genre = input("Ok, which genre would you like to know about?\n").strip().lower().title()
            details = Genre.getGenreDetails(genre)
            print(f"Here are the details for the genre '{genre}':")
            print(f" - '{details}'")
            
        elif choice == "display all":
            print("\nOk, lets display all genres..\n")
            Genre.displayAllGenres()

        elif choice == "books of genre":
            print("\nOk, here's a list of all our genres:\n")
            Genre.displayAllGenres()
            genre = input("\nWhich genre would you like to view the books of?\n").strip().lower().title()
            Genre.viewGenreBooks(genre)

        elif choice == "exit":
            print("\nReturning to previous menu...\n")
            continue

        else:
            print("\nReturning to previous menu...\n")
            continue
        
    if action == "quit":
        print("\nGoodbye! Thanks for reading!\n")
        break

