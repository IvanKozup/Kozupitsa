if __name__ == "__main__":
    # Write your solution here
    class Parking:
        """ Базовый класс Парковки

        :param park_space: Количество парковочных мест - публичный атрибут
        :param bear_capacity: Несущая способность паркинга - публичный атрибут
        :param aver_weight_auto: Средний вес авто в тоннах - непубличный атрибут

        Инкапсуляция используется для сохранности кода других польззователей
        в связи с вероятным переименованием
        """
        def __init__(
                self,
                park_space: int,
                bear_capacity: float,
                aver_weight_auto: float
                    ):
            self.park_space = park_space
            self.bear_capacity = bear_capacity
            self._aver_weight_auto = aver_weight_auto

        def __str__(self) -> str:
            return (
                f"Парковка на {self._park_space} несущей способностью {self._bear_capacity}")

        def __repr__(self) -> str:
            return (
                f"{self.__class__.__name__}(park_space={self._park_space}, bear_capacity={self._bear_capacity})")

        @property
        def park_space(self):
            return self._park_space

        @park_space.setter
        def park_space(self, space):
            if not isinstance(space, int):
                raise TypeError("Количество мест должно быть целочисленного типа")
            if space <= 0:
                raise ValueError("Количество мест должно быть больше нуля")
            self._park_space = space

        @property
        def bear_capacity(self):
            return self._bear_capacity

        @bear_capacity.setter
        def bear_capacity(self, bear):
            if not isinstance(bear, float):
                raise TypeError("Несущая способность должна быть с плавающей запятой")
            if bear <= 0:
                raise ValueError("Несущая способность должна быть больше нуля")
            self._bear_capacity = bear

        @property
        def aver_weight_auto(self):
            return self._aver_weight_auto

        @aver_weight_auto.setter
        def aver_weight_auto(self, weight):
            if not isinstance(weight, float):
                raise TypeError("Средний вес машины должен быть с плавающей запятой")
            if weight <= 0:
                raise ValueError("Средней вес машины должен быть больше нуля")
            self._aver_weight_auto = weight

        def capacity_check(self, num_auto: int) -> bool:
            """
            Метод проверяет справится ли парковка с точки зрения несущей способности
            с нагрузкой от заданного количества авто

            :param num_auto: Количество автомобилей на парковке
            :return: True - условие выполняется; False - не выполняется
            """
            return num_auto * self._aver_weight_auto < self.bear_capacity

        def potential_profit(self, space_cost: float, expenses: float) -> float:
            """
            Метод находит потенциальную прибыль парковки при полной занятости мест

            :param space_cost: Стоимость места на парковке за месяц
            :param expenses: Затраты парковки за месяц
            :return: Потенциальную прибыль парковки с полной загрузкой
            """
            return self.park_space * space_cost - expenses


    class Electrical(Parking):
        """ Дочерний класс Парковка под электрические машины

        :param park_space: Количество парковочных мест - публичный атрибут
        :param bear_capacity: Несущая способность паркинга - публичный атрибут
        :param weight_electric: Средний вес электронной машины - непубличный атрибут

        Инкапсуляция используется для сохранности кода других польззователей
        в связи с вероятным переименованием
        """
        def __init__(
                self,
                park_space: int,
                bear_capacity: float,
                weight_electric: float
                    ):
            super().__init__(park_space, bear_capacity)
            self.weight_electric = weight_electric

        def __str__(self) -> str:
            return f"Парковка для эл.машин на {self._park_space} мест несущей способностью {self._bear_capacity}"

        @property
        def weight_electric(self):
            return self._weight_electric

        @weight_electric.setter
        def weight_electric(self, e_weight):
            if not isinstance(e_weight, float):
                raise TypeError("Средний вес машины должен быть с плавающей запятой")
            if e_weight <= 0:
                raise ValueError("Средней вес машины должен быть больше нуля")
            self._weight_electric = e_weight

        def capacity_check(self, el_num_auto: int) -> bool:
            """
            Метод проверяет справится ли парковка с точки зрения несущей способности
            с нагрузкой от заданного количества электронного авто

            :param el_num_auto: Количество электронных машин
            :return: True - условие выполняется; False - не выполняется
            """
            return el_num_auto * self._weight_electric < self.bear_capacity

    pass
