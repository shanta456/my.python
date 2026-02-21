class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.book_dict = {}

    def addBook(self, adbook):
        self.list_of_books.append(adbook)

    def displayBook(self):
        count = 1
        print("Available books are:")
        for i in self.list_of_books:
            print(f"{count}. {i}")
            count += 1

        print("Currently unavailable books are:")
        count = 1
        for key, value in self.book_dict.items():
            print(f"{count}.'{key}' book is issued to '{value}'")
            count += 1

    def lendBook(self, book_name, name_of_person):

        if book_name in self.list_of_books:
            print(f"The '{book_name}' is issued to '{name_of_person}'.")
            self.book_dict[book_name] = name_of_person
            self.list_of_books.remove(book_name)
        else:
            name = self.book_dict.get(book_name)
            print(f"The {book_name} is already issued to {name}")

    def returnBook(self, book):
        if book in self.book_dict.keys():
            self.list_of_books.append(book)
            del self.book_dict[book]
            print("Book returned")
        else:
            print(f"This {book} book isn't issued from here.")


testlib = Library(['python','c++ basics','Harry Pottel'], "TestLib")

print("Type:\n1.display ---> To display list of available books.\n2.lend ---> To lend a"
"book from library.\n3.add ---> To add new book to library.\n4.return ---> To return a book to library.\n3.lend ---> To lend a"
"book from library.\n5.exit ---> To exit the program.")


while True:
    user=input()
    if user == "display":
        testlib.displayBook()
        print("\nBook(s) displayed.")
        
    elif user == "lend":
        bname = input("Enter book to be issued: ")
        uname = input("Enter your name: ")
        testlib.lendBook(bname, uname)
    elif user == "add":
        new_book = input("Enter book name to be added: ")
        testlib.addBook(new_book)
        print(f"'{new_book}' book added to the library.")
    elif user == "return":
        book_name = input("Enter book name to be returned: ")
        testlib.returnBook(book_name)
    elif user == "exit":
        print("Exiting the program.")
        break
    else:
        print("Wrong input.")