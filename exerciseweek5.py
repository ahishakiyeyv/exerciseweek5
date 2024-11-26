class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def read(self):
        return f"You're reading '{self.title}' by {self.author}."

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, Genre: {self.genre}."


# class with inheritance
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size 

    def read(self):
        return f"You're reading the eBook '{self.title}' on your device."

    def download(self):
        return f"Downloading '{self.title}', File Size: {self.file_size}MB."
    

# Usage example
print("Assignment 1:")
book = Book("1984", "George Orwell", 328, "Dystopian")
ebook = EBook("Digital Fortress", "Dan Brown", 356, "Thriller", 5)

print(book.read())
print(book)
print(ebook.read())
print(ebook.download())
