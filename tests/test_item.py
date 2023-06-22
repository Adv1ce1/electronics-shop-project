from src.item import Item
import pytest
from src.instantiatecsverror import InstantiateCSVError


def test_item1_name(item1):
    assert item1.name == 'Ноутбук'


def test_item1_name_change(item1):
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_item1_price(item1):
    assert item1.price == 1000.0


def test_item1_quantity(item1):
    assert item1.quantity == 5


def test_item1_total_price(item1):
    assert item1.calculate_total_price() == 5000.0


def test_item1_discount(item1):
    item1.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 900.0


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("src/items.csv")


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items_failed.csv")


def test_item1_from_csv_name():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item1_repr(item2):
    assert repr(item2) == "Item('Смартфон', 10000, 20)"


def test_item1_str(item2):
    assert str(item2) == 'Смартфон'