class booknotavailable:
    def __init__(self,book):
        self.book = book

    def check(self):
        if self.book.bookstores==[]:
            print("No books available")
            return False
        else:
            return True
        