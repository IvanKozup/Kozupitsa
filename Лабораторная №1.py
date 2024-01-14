# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Site:
    def __init__(self, value_workers: int, require_workers: int):
        """
        Создание и подготовка к работе объекта "Площадка"

        :param value_workers: Кол-во строителей на площадке
        :param require_workers: Необходимое кол-во строителей для выполнения работ

        Примеры:
        >>> site = Site(25, 20)  # инициализация экземпляра класса
        """
        if not isinstance(value_workers, int):
            raise TypeError("Кол-во строителей должно быть типа int")
        if value_workers < 0:
            raise ValueError("Кол-во строителей должно быть больше или равно нулю")
        self.value_workers = value_workers

        if not isinstance(require_workers, int):
            raise TypeError("Требуемое кол-во строителей должно быть типа int")
        if require_workers < 0:
            raise ValueError("Требуемое кол-во строителей должно быть больше или равно нулю")
        self.require_workers = require_workers



    def will_work_be_done(self) -> bool:
        """
        Функция которая проверяет хватит ли рабочих для выполнения работ

        :return: Хватит ли рабочих для выполнения работ

        Примеры:
        >>> site = Site(14, 8)
        >>> site.will_work_be_done()
        """
        ...

    def smoke_break(self, smoke_workers: int) -> int:
        """
        Проверка количества работающих людей во время перекура
        :param smoke_workers: Кол-во курящих строителей
        :raise ValueError: Если кол-во курящих превышает кол-во людей на стройке, то вызываем ошибку

        :return: Количество работающих людей на стройке

        Примеры:
        >>> site = Site(8, 3)
        >>> site.smoke_break(4)
        """
        if not isinstance(smoke_workers, int):
            raise TypeError("Кол-во курящих строителей должно быть типа int")
        if smoke_workers < 0:
            raise ValueError("Кол-во курящих строителей должно быть больше или равно нулю")
        ...


class Environment:
    def __init__(self, construction_area: float, green_area: float):
        """
        Создание и подготовка к работе объекта "Планировка участка"

        :param construction_area: Площадь территории объекта
        :param green_area: Площадь озеленения

        :raise ValueError: Если площадь озеленения больше площади территории объекта, то вызываем ошибку

        Примеры:
        >>> environment = Environment(150, 49.8)  # инициализация экземпляра класса
        """
        if not isinstance(construction_area, (int, float)):
            raise TypeError("Площадь территории должна быть типа int или float")
        if construction_area <= 0:
            raise ValueError("Площадь территории должна быть больше нуля")
        self.construction_area = construction_area

        if not isinstance(green_area, (int, float)):
            raise TypeError("Площадь озеленения должна быть типа int или float")
        if green_area < 0:
            raise ValueError("Площадь озеленения должна быть больше или равно нулю")
        self.green_area = green_area



    def percentage_green(self) -> float:
        """
        Функция которая вычисляет отношение площади озеленения к площади объекта

        :return: Отношение площади озеленения к площади объекта

        Примеры:
        >>> environment = Environment(148.2, 8)
        >>> environment.percentage_green()
        """
        ...

    def percentage_building(self, building_area: (int, float)) -> float:
        """
        Функция которая вычисляет отношение застроенной площади к площади трритории объекта
        :param building_area: Застроенная площадь

        :raise ValueError: Если сумма застроенной площади и площади озеленения больше площади территории объекта, то вызываем ошибку

        :return: Отношение застроенной площади к площади трритории объекта

        Примеры:
        >>> environment = Environment(13000.08, 245)
        >>> environment.percentage_building(10000.1)
        """
        if not isinstance(building_area, (int, float)):
            raise TypeError("Застроенная площадь должна быть типа int или float")
        if building_area <= 0:
            raise ValueError("Застроенная площадь должна быть больше нуля")
        ...


class Copybook:
    def __init__(self, amount_sheets: int, pulled_out_sheets: int):
        """
        Создание и подготовка к работе объекта "Тетрадь"

        :param amount_sheets: Количество листов
        :param pulled_out_sheets: Количество вырванных листов

        :raise ValueError: Если количество вырванных листов больше или равно количеству листов, то вызываем ошибку

        Примеры:
        >>> copybook = Copybook(24, 2)  # инициализация экземпляра класса
        """
        if not isinstance(amount_sheets, int):
            raise TypeError("Количество листов должно быть типа int")
        if amount_sheets <= 0:
            raise ValueError("Количество листов должно быть больше нуля")
        self.amount_sheets = amount_sheets

        if not isinstance(pulled_out_sheets, (int, float)):
            raise TypeError("Количество вырванных листов должно быть типа int")
        if pulled_out_sheets < 0:
            raise ValueError("Количество вырванных листов должно быть больше или равно нулю")
        self.pulled_out_sheets = pulled_out_sheets



    def sheets_in_copybook(self) -> int:
        """
        Функция которая вычисляет количество оставшихся листов в тетради

        :return: Количество оставшихся листов в тетради

        Примеры:
        >>> copybook = Copybook(64, 20)
        >>> copybook.sheets_in_copybook()
        """
        ...

    def cleen_sheets(self, written_sheets: int) -> int:
        """
        Функция которая вычисляет количество чистых листов в тетради
        :param written_sheets: Исписанные листы

        :raise ValueError: Если сумма исписанных и вырванных листов больше количества листов в тетради, то вызываем ошибку

        :return: Количество чистых листов в тетради

        Примеры:
        >>> copybook = Copybook(48, 0)
        >>> copybook.cleen_sheets(23)
        """
        if not isinstance(written_sheets, int):
            raise TypeError("Количество исписанных листов должно быть типа int")
        if written_sheets < 0:
            raise ValueError("Количество вырванных листов должно быть больше или равно нулю")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass