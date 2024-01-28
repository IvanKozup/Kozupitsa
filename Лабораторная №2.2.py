BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id        # Идентификатор книги
        self.name = name    # Название книги
        self.pages = pages  # Количество страниц в книге

    def __str__(self) -> str:
        # Книга "название_книги"
        return f'Книга "{self.name}"'

    def __repr__(self):
        # Book(id_=1, name='test_name_1', pages=200)
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        self.books = books

    def get_next_book_id(self):
        if self.books is None:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        for i, x in enumerate(self.books):
            if x.id == book_id:
                return i
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
