from typing import List, Tuple

import pytest


# фикстуры для tests_masks
@pytest.fixture
def valid_card_data() -> List[Tuple[str, str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("0000111122223333", "0000 11** **** 3333"),
        ("4444555566667777", "4444 55** **** 7777"),
    ]


@pytest.fixture
def invalid_card_data() -> List[Tuple[str, str]]:
    return [
        ("1234 567", "Неверный номер карты"),
        ("abcd efgh ijkl mnop", "Неверный номер карты"),
        ("1234 5678 1234 567", "Неверный номер карты"),
        ("1234 5678 1234 56789", "Неверный номер карты"),
        ("", "Неверный номер карты"),
    ]


@pytest.fixture
def valid_account_data() -> List[Tuple[str, str]]:
    return [
        ("1234567890123456", "**3456"),
        ("9876543210987654", "**7654"),
        ("0000000000000000", "**0000"),
        ("1111222233334444", "**4444"),
    ]


@pytest.fixture
def invalid_account_data() -> List[Tuple[str, str]]:
    return [
        ("123", "**123"),
        ("abcd", "**abcd"),
        ("12", "**12"),
        ("", "**"),
    ]


# Фикстуры для test_widget


@pytest.fixture
def valid_card_data_set() -> List[Tuple[str, str]]:
    return [
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Visa 0000000000000000", "Visa 0000 00** **** 0000"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ]


@pytest.fixture
def valid_account_data_set() -> List[Tuple[str, str]]:
    return [
        ("Счет 1234567890123456", "Счет **3456"),
        ("Счет 9876543210987654", "Счет **7654"),
        ("Счет 0000000000000000", "Счет **0000"),
    ]


@pytest.fixture
def invalid_data_set() -> List[Tuple[str, str]]:
    return [
        ("Visa Classic 12345678", "Неверный номер карты"),
        ("MasterCard 1234 5678 1234", "Неверный номер карты"),
        ("Счет 123", "Счет **123"),
    ]
