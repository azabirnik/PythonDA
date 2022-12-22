# Aleksei Zabirnik <azabirnik@gmail.com>
# Avito Academy homework 4

from typing import Union, Any
from keyword import iskeyword
import json


class PythonObjectFromDict:
    """ Decomposes Json objects into Python objects """
    def __init__(self, mappings: dict[str, Any]) -> None:
        for property_name, value in mappings.items():
            if not property_name or not isinstance(property_name, str):
                raise ValueError(
                    f'"{type(property_name)}"'
                    ' is not a valid object for property name.'
                )
            if not property_name.isidentifier():
                raise ValueError(
                    f'"{property_name}" in not'''
                    ' a valid python name for property.'
                )
            if iskeyword(property_name):
                property_name = property_name + '_'
            if isinstance(value, dict):
                setattr(self, property_name, PythonObjectFromDict(value))
            else:
                setattr(self, property_name, value)


class Advert(PythonObjectFromDict):
    """ A class for adverts """
    def __init__(self, mappings: dict[str, Any]) -> None:
        super().__init__(mappings)
        if not hasattr(self, 'title'):
            raise ValueError(
                '"title" is a mandatory property'
                ' and must be set.'
            )
        if hasattr(self, 'price'):
            if self.price < 0:
                raise ValueError(
                    '"price" must be non negative'
                    f' but set to "{self.price}".'
                )
        else:
            self.price = 0

    def __repr__(self):
        """ Basic representation for an advert """
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: Union[int, float]) -> None:
        if not isinstance(new_price, int) and not isinstance(new_price, float):
            raise ValueError(
                f'"price" must be numeric but got {type(new_price)}.'
            )
        if new_price < 0:
            raise ValueError(
                f'"price" must be non negative, not "{new_price}".'
            )
        self._price = new_price


class ColorizeMixin:
    """ This mixin is used to colorize any class """
    repr_color_code = 32  # green

    def __repr__(self) -> str:
        """" Colorize with repr_color_code """
        return (
            f'\033[1;{self.repr_color_code};'
            f'40m{super().__repr__()}\033[0m'
        )


class ColorAdvert(ColorizeMixin, Advert):
    """ Colored adverts, set repr_color_code in Json to colorize advert """


if __name__ == '__main__':
    print('Test 1:')
    lesson_str = """{
        "title": "python",
        "price": 0,
        "class": 120,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.class_)
    lesson_ad.price = 121.10
    print(lesson_ad.price)
    try:
        lesson_ad.price = -1
    except ValueError:
        print('Got ValueError as intended.')

    print('\nTest 2:')
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
    except ValueError:
        print('Got ValueError as intended.')

    print('\nTest 3:')
    lesson_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "repr_color_code": 33,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское,\
 поселок санатория Тишково, 25"
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = ColorAdvert(lesson)
    print(lesson_ad)
