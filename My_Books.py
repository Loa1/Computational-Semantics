import Book
import Quicksort

got = Book.Book('A Game of Thrones', Book.Author('George R. R.', 'Martin'), '978-0553573404', 694)
hp = Book.Book('Harry Potter and the Philosophers Stone', Book.Author('Joanne K.', 'Rowling'), '978-1408855652', 331)
lotr = Book.Book('Lord of the Rings: The Fellowship of the Rings', Book.Author('John Ronald Reuel', 'Tolkien'), '978-0261102354', 529)


library = [got, hp, lotr]

Quicksort.quicksort(library)

for n in library:
	print(str(n) + "\n")






