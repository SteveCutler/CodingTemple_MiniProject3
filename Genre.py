from Book import Book

class Genre:
    def __init__(self, name, description):
        self.name = name
        self.__description = description
    
    def addNew(name):
        if name in Genres.keys():
            print(f"Found '{name}' in Genres list!")
        else:
            description = input(f"\nPlease enter a one sentence description of the Genre '{name}':\n")
            Genres[name] = Genre(name,description)
            print(f"\n Genre '{name}' added to database!")
    
    def getGenreDetails(genre):
        return Genres[genre].__description

    def viewGenreBooks(genre):
        for book, details in Book.LibraryBooks.items():
            if details.genre == genre:
                print(details.title)
    
    def displayAllGenres():
        for genre in Genres.keys():
            print(genre)


    
Genres = {"Fantasy": Genre("Fantasy", "Strange new worlds, magic spells, quests. Inner journeys manifested externally."), "Science Fiction": Genre("Science Fiction", "Brain Boggling books about the near to distant future. Often with dystopian or tragic themes."), "Horror": Genre("Horror", "Scary books about ghosts, murderers and other spooky subjects!"), "Romance": Genre("Romance", "Romantic books about love, unrequited love, adventures, drama, etc"), "Mystery": Genre("Mystery", "Mysterious disappearances, disenchanted detectives, spiralling plots, crazy dames, etc")}