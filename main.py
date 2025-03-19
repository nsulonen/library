class Book:
    def __init__(self, title: str, author: str, isbn: str, is_available: bool = True) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn

    def __repr__(self) -> str:
        return f"\nBook: {self.title}, {self.author}, {self.isbn}, is.available = {self.is_available}"

    def __getitem__(self, item):
        pass

    def check_out(self) -> None:
        self.is_available = False

    def return_book(self) -> None:
        self.is_available = True

class Member:
    def __init__(self, name: str, member_id: str, borrowed_books: list[Book] | None = None) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def __repr__(self) -> str:
        return f"\nMember: {self.name}, id: {self.member_id}"

    def borrow_book(self, book: Book) -> None:
        if book.is_available:
            self.borrowed_books.append(book)
            book.check_out()
        else:
            print("Book is not available")

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)



class Library:
    def __init__(self, books: list[Book], members: list[Member]) -> None:
        self.books = books
        self.members = members

    def __repr__(self) -> str:
        return f"\nLibrary books={self.books}\n\nLibrary members={self.members}"

    def add_book(self, title: str, author: str, isbn: str) -> None:
        pass

    def remove_book(self):
        pass

    def search_book(self):
        pass

    def register_member(self, name: str, member_id: str) -> None:
        self.members.append(Member(name, member_id))

def main() -> None:
    book: Book = Book("Python Basics", "John", "123A")
    member: Member = Member("Simon", "M1")
    library: Library = Library([book], [member])

    member.borrow_book(book)
    print(member.borrowed_books)
    member.borrow_book(book)
    library.add_book("Programming", "John", "123B")
    print(library)
    member.return_book(book)
    print(library)
if __name__ == "__main__":
    main()