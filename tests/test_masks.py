from typing import List, Tuple

import pytest

from src.masks import card_mask, number_account_mask


@pytest.mark.parametrize(
    "number_card, expected_output",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_card_mask(card_data: List[Tuple[str, str]], number_card: str, expected_output: str) -> None:
    assert card_mask(number_card) == expected_output


@pytest.mark.parametrize(
    "number_card",
    [
        "12345678",
        "1234 5678 1234",
        "000000000000000",
        "1111 2222 3333 444",
    ],
)
def test_invalid_card_mask(invalid_card_data: List[str], number_card: str) -> None:
    assert card_mask(number_card) == "Неверный номер карты"


@pytest.mark.parametrize(
    "number_account, expected_output",
    [
        ("1234567890123456", "**3456"),
        ("9876543210987654", "**7654"),
        ("0000000000000000", "**0000"),
        ("1111222233334444", "**4444"),
        ("1234", "**1234"),
    ],
)
def test_number_account_mask(account_data: List[Tuple[str, str]], number_account: str, expected_output: str) -> None:
    assert number_account_mask(number_account) == expected_output


@pytest.mark.parametrize(
    "number_account",
    [
        "",
        "123",
        "abcde",
        "12ab34cd",
    ],
)
def test_invalid_number_account_mask(invalid_account_data: List[str], number_account: str) -> None:
    assert number_account_mask(number_account) == "**" + number_account[-4:]



