from src.item import Item


class LanguageMixin:
    """
    Миксин для поддержки изменения языка (раскладки клавиатуры).

        __language - язык расскладки клавиавтуры, по умолчанию 'EN'
    """

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self) -> str:
        """
        Возвращает текущий язык (раскладку клавиатуры).

        :return: Текущий язык.
        """
        return self.__language

    def change_lang(self):
        self.__language = "RU" if self.language == "EN" else "EN"
        return self


class KeyBoard(Item, LanguageMixin):
    """
    Класс, представляющий клавиатуру в магазине.
    Наследует все атрибуты класса Item и добавляет атрибуты и методы для работы с языком (раскладкой клавиатуры).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создает экземпляр класса Keyboard.

        :param name: Название клавиатуры.
        :param price: Цена за единицу клавиатуры.
        :param quantity: Количество клавиатур в магазине.

        __language - язык расскладки клавиавтуры, по умолчанию 'EN'
        """
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)