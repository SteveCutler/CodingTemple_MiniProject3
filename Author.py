class Author:
    def __init__(self, name, bio):
        self.name = name
        self.__bio = bio

    def addAuthor(name):
        if name in authors:
            print(f"'{name}' is already in our authors database!")
        else:
            bio = input("Please enter a one sentence bio for the author:\n").strip().capitalize()
            authors[name] = Author(name,bio)
            print(f"\nAuthor '{name}' added to database!")
        

    def getAuthorDetails(name):
        if name in authors:
            print(authors[name].__bio)
        else:
            print(f"\nSorry, couldn't find {name} in our authors database!\n")

    def displayAllAuthors():
        for author in authors.keys():
            print(f" - {author}")


authors = {"JK Rowling": Author("JK Rowling","Author of the world famous Harry Potter series.."), "Robert Louis Stevenson": Author("Robert Louis Stevenson", "19th century author, famous for writing the novel 'Treasure Island'"), "George Orwell": Author("George Orwell","Mid 20th century novelist, famous for writing '1984', 'Animal Farm', 'Down and out in Paris and London', etc.")}