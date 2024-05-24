from typing import List, Tuple

import pytest


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
