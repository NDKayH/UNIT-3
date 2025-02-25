# Quiz 048


## Paper Solution
![IMG_4793](https://github.com/user-attachments/assets/a997f7de-6b24-44ae-b1c6-5a22c331905c)

## Code
```.py

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()
                print("----------")  # Separator for readability


# Example
if __name__ == "__main__":
    my_library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    my_library.add_book(book1)
    my_library.add_book(book2)

    my_library.show_books()

```

## Proof of work
![image](https://github.com/user-attachments/assets/f611facb-1ee0-4fe3-93b8-0f7173e9e582)

