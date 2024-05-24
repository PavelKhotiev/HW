import pytest

from src.masks import card_mask, number_account_mask


@pytest.mark.parametrize(
    "number_card, expected_output",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("0000111122223333", "0000 11** **** 3333"),
        ("4444555566667777", "4444 55** **** 7777"),
    ],
)
def test_card_mask_valid(number_card: str, expected_output: str) -> None:
    assert card_mask(number_card) == expected_output


@pytest.mark.parametrize(
    "number_card, expected_output",
    [
        ("1234 567", "Неверный номер карты"),
        ("abcd efgh ijkl mnop", "Неверный номер карты"),
        ("1234 5678 1234 567", "Неверный номер карты"),
        ("1234 5678 1234 56789", "Неверный номер карты"),
        ("", "Неверный номер карты"),
    ],
)
def test_card_mask_invalid(number_card: str, expected_output: str) -> None:
    assert card_mask(number_card) == expected_output

    # тест для ф-ции счета


@pytest.mark.parametrize(
    "number_account, expected_mask",
    [
        ("1234567890123456", "**3456"),
        ("9876543210987654", "**7654"),
        ("0000000000000000", "**0000"),
        ("1111222233334444", "**4444"),
    ],
)
def test_number_account_mask_valid(number_account: str, expected_mask: str) -> None:
    assert number_account_mask(number_account) == expected_mask


@pytest.mark.parametrize(
    "number_account, expected_mask",
    [
        ("123", "**123"),
        ("abcd", "**abcd"),
        ("12", "**12"),
        ("", "**"),
    ],
)
def test_number_account_mask_invalid(number_account: str, expected_mask: str) -> None:
    assert number_account_mask(number_account) == expected_mask
