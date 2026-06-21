import books
class error:
    def __init__(self):
        self.bookstores=books.books.bookstores

    def check(self):
        if self.bookstores==[]:
            print("No books available")
            return False
        else:
            return True
        