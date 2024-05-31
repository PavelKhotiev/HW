import pytest

from src.widget import mask_card_or_account


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Visa 0000000000000000", "Visa 0000 00** **** 0000"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ],
)
def test_mask_card_or_account_valid_card(input_str: str, expected_output: str) -> None:
    assert mask_card_or_account(input_str) == expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Счет 1234567890123456", "Счет **3456"),
        ("Счет 9876543210987654", "Счет **7654"),
        ("Счет 0000000000000000", "Счет **0000"),
    ],
)
def test_mask_card_or_account_valid_account(input_str: str, expected_output: str) -> None:
    assert mask_card_or_account(input_str) == expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Visa Classic 12345678", "Неверный номер карты"),
        ("MasterCard 1234 5678 1234", "Неверный номер карты"),
        ("Счет 123", "Счет **123"),
    ],
)
def test_mask_card_or_account_invalid(input_str: str, expected_output: str) -> None:
    assert mask_card_or_account(input_str) == expected_output
