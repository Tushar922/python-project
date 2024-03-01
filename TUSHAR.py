# we will create class
class Library:
  # a constructer in python
  def __init__(self):
    self.noBooks = 0
    self.books = []
  # we will make a function to add books to library management system
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)
  # This function will show information about library
  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)

# we will use variable to use our code 
l1 = Library()
# and we will use our  hand made function
l1.addBook("opo1")
l1.addBook("oer2")
l1.addBook("Harry Potter7")
l1.showInfo()
# done bye have a great day