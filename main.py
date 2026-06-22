import menu
import empty

class library:
    
    def __init__(self):
        self.book = menu.books()
        self.empty = empty.booknotavailable(self.book)  

    def menu(self):
        while True:
            num = input("enter 1 for add book\nenter 2 for edit book\nenter 3 for remove book\nenter 4 for search book\nenter 5 for display all book\nenter 6 for exit\nenter the option:\t")
            print("*"*50)
            match num:
                case "1":
                    nob=int(input("enter the num of books:\t"))
                    
                    for i in range (nob):
                        self.book.addbook()
                    self.book.display()
                case "2":
                    if self.empty.check():
                        self.book.edit()
                        self.book.display()
                case "3":
                    if self.empty.check():
                        self.book.remove()
                        self.book.display()
                case "4":
                    if self.empty.check():
                        self.book.search()
                        self.book.display()
                case "5":
                    if self.empty.check():
                        self.book.display()
                case "6":
                    break
                case _:
                    print("invalid input")


lib = library()
lib.menu()
