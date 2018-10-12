class Book:
    
    def __init__(self, name, author, isbn, pages):
        self.name = name
        self.authors = []
        self.authors.append(author)
        self.isbn = isbn
        self.pages = pages
    
    def add_author(self, first):
        self.authors.append(author)
    
    def __gt__(self, other):
        return self.pages > other.pages

    def __eq__(self, other):
        return self.pages == other.pages
    
    def __str__(self):
        res = "Booktitle: " + self.name + "\nAuthors: "
        for n in self.authors:
            res = res + "\n" + str(n)
        
        res = res + "\nISBN: " + self.isbn + "\nNumber of Pages: " + str(self.pages)
        return res
    
    
class Author:
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        return str(self.firstname) + " " + self.lastname