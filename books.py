
class books:
    bookstores=[]
    def __init__(self):
        pass
    def books(self):
        numofbook=int(input("num of books:"))
        for i in range(numofbook):
            self.book_name=input("enter the book name:")
            self.author=input("enter the author name:")
            self.price=int(input("enter the price:"))
            self.isbn=int(input("enter the isbn:"))
            self.bookstores.append({"book_name": self.book_name, "author": self.author, "price": self.price, "isbn": self.isbn})
            print(f"{self.bookstores}\n")
    def edit(self):
        bookname=input("enter the name of the book you want to edit:")
        for book in self.bookstores:
            if book["book_name"]==bookname:
                book["book_name"]=input("enter the new book name:")
                book["author"]=input("enter the new author name:")
                book["price"]=int(input("enter the new price:"))
                book["isbn"]=int(input("enter the new isbn:"))
                print(f"{self.bookstores}\n")

    def remove(self):
        bookname=input("enter the name of the book you want to remove:")
        for book in self.bookstores:
            if book["book_name"]==bookname:
                self.bookstores.remove(book)
                print(f"{self.bookstores}\n")
                break
    def search(self):
        bookname=input("enter the name of the book you want to search:")
        for book in self.bookstores:
            if book["book_name"]==bookname:
                print(f"{book}\n")

    def display(self):
        print(f"{self.bookstores}\n")
