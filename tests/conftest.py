import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


@pytest.fixture
def item1():
    return Item('Ноутбук', 1000.0, 5)


@pytest.fixture
def item2():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120000.0, 2, 5)


@pytest.fixture
def keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    return kb