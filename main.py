import books
import empty

class library:
    def __init__(self):
        self.book = books.books()

    def menu(self):
        while True:
            num = int(input("enter 1 for add book\nenter 2 for edit book\nenter 3 for remove book\nenter 4 for search book\nenter 5 for display all book\nenter 6 for exit:\n "))
            
            match num:
                case 1:
                    self.book.books()
                case 2:
                    if empty.error().check():
                        self.book.edit()
                case 3:
                    if empty.error().check():
                        self.book.remove()
                case 4:
                    if empty.error().check():
                        self.book.search()
                case 5:
                    if empty.error().check():
                        self.book.display()
                case 6:
                    break
                case _:
                    print("invalid input")


lib = library()
lib.menu()
