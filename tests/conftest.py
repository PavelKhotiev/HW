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


# Фикстуры для processing


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "FAILED"},
    ]


# Фикстуры для generators
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
