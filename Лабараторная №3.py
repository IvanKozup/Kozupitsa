class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """ Дочерний класс книги (бумажная). """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, n_pages):
        if not isinstance(n_pages, int):
            raise TypeError("Количество страниц должно быть целочисленного типа")
        if n_pages <= 0:
            raise ValueError("Количество страниц в книге должно быть больше нуля")


class AudioBook(Book):
    """ Дочерний класс книги (Аудио). """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __str__(self):
        return f"Аудионига {self.name}. Автор {self.author}"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, n_duration):
        if not isinstance(n_duration, int):
            raise TypeError("Продолжительность должна быть целочисленного типа")
        if n_duration <= 0:
            raise ValueError("Продолжительность книги должна быть больше нуля")
