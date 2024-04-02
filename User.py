
class User:
    
    def __init__(self, name, address):
        self.name = name
        self.__address = address
        self.__books = {}

    def addUser(name):
        if name in Users:
            print(f"Found user '{name}' in our system...")
        else:
            print(f"Lets register user '{name}' so you can borrow books..\n")
            address = input(f"What address would you like to put on file for {name}\n").strip().lower().title()
            Users[name] = User(name, address)
            print(f"User '{name}' added to database...\n")

    def getUserBooks(name):
        if Users[name].__books:
            bookList = []
            for book in Users[name].__books.keys():
                bookList.append(book)
            return bookList
        else:
            print(f"It doesn't look like user '{name}' has any borrowed books!\n")

    def setUserBooks(user, book, function):

        if user not in Users:
            print(f"The user '{user}' doesn't appear to be in our system!\n")
            
        elif function == "add":
            Users[user].__books[book.title] = book

        else: 
            del Users[user].__books[book.title]

    def getUserDetails(name):
        if name not in Users:
            print(f"The user '{name}' doesn't appear to be in our system!\n")
        else:
            print(f" - {Users[name].name}, {Users[name].__address}")
            if Users[name].__books:
                print(f"\nHeres a list of books {name} currently has borrowed:")
                bookList = User.getUserBooks(name)
                for book in bookList:
                    print(f" -{book}")
                print("\n")

    def displayAllUsers():
        if Users:
            print("\nHere's a list of all users currently registered:")
            for user in Users.keys():
                print(user)
        else: 
            print("There are currently no users registered!")


Users = {}


#         1. Add a new user
#         2. View user details
#         3. Display all users
