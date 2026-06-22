class Book:
    def __init__(self,id, bookname, author, price, isbn):
        self.id=id
        self.bookname = bookname
        self.author = author
        self.price = price
        self.isbn = isbn


class books:
    id=1
    def __init__(self):
        self.bookstores=[]
    def addbook(self):
        bookname=input("enter the book name:\t")
        author=input("enter the author name:\t")
        price=int(input("enter the price:\t"))
        isbn=int(input("enter the isbn:\t\t"))
        
        new_book = Book(books.id,bookname, author, price, isbn)
        self.bookstores.append(new_book)
        books.id+=1
        print("Book added successfully!\n")
        print("*"*50)   

    def edit(self):
        bookid=int(input("enter the id of the book you want to edit:\t"))
        for book in self.bookstores:
            if book.id==bookid:
                book.bookname=input("enter the new book name:\t")
                book.author=input("enter the new author name:\t")
                book.price=int(input("enter the new price:\t\t"))
                book.isbn=int(input("enter the new isbn:\t\t"))
                print("Book updated successfully!\n")
                break
        else:
            print("book not found\n") 
        print("*"*50)

    def remove(self):
        bookid=int(input("enter the id of the book you want to remove:\t"))
        for book in self.bookstores:
            if book.id==bookid:
                self.bookstores.remove(book)
                print("Book removed successfully!\n")
                break
        else:
            print("book not found\n")
        print("*"*50)

    def search(self):
        bookid=int(input("enter the id of the book you want to search:\t"))
        for book in self.bookstores:
            if book.id==bookid:
                print(f"[ID: {book.id},Name: {book.bookname}, Author: {book.author}, Price: {book.price}, ISBN: {book.isbn}]\n")
                break   
        else:
            print("book not found\n")
        print("*"*50)

    def display(self):
        if self.bookstores==[]:
            print("No books available")
        else:
            for book in self.bookstores:
                print(f"[ID: {book.id},Name: {book.bookname}, Author: {book.author}, Price: {book.price}, ISBN: {book.isbn}]")
        print("*"*50)
