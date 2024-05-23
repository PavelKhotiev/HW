import pytest

from src.widget import mask_card_or_account, format_date


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Visa 0000000000000000", "Visa 0000 00** **** 0000"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
        ("Счет 1234567890123456", "Счет **3456"),
        ("Счет 9876543210987654", "Счет **7654"),
        ("Счет 0000000000000000", "Счет **0000"),
        ("Счет 1111222233334444", "Счет **4444"),
        ("Счет 1234", "Счет **1234"),
    ],
)
def test_mask_card_or_account(card_data, account_data, input_str, expected_output):
    assert mask_card_or_account(input_str) == expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Visa Classic 12345678", "Неверный номер карты"),
        ("MasterCard 1234 5678 1234", "Неверный номер карты"),
    ],
)
def test_invalid_mask_card_or_account(invalid_data, input_str, expected_output):
    assert mask_card_or_account(input_str) == expected_output


@pytest.mark.parametrize(
    "date_str, expected_output",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2022-02-28T12:00:00.000000", "28.02.2022"),
        ("2023-03-15T12:30:45.123456", "15.03.2023"),
    ]
)
def test_format_date_valid(date_str: str, expected_output: str) -> None:
    assert format_date(date_str) == expected_output


@pytest.mark.parametrize(
    "date_str, expected_output",
    [
        ("2018-07-1T02:26:18.671407", "Неверный формат даты"),
        ("2020-01-32T00:00:00.000000", "Неверный формат даты"),
        ("abcd-ef-ghTij:kl:mn.opqrst", "Неверный формат даты"),
        ("2021-02-29T12:00:00.000000", "Неверный формат даты"),
        ("2020-04-31T12:00:00.000000", "Неверный формат даты"),
        ("2019-02-29T12:00:00.000000", "Неверный формат даты"),
        ("20200101T000000.000000", "Неверный формат даты"),
        ("2020-01-01", "Неверный формат даты"),
        ("", "Неверный формат даты"),
    ]
)
def test_format_date_invalid(date_str: str, expected_output: str) -> None:
    assert format_date(date_str) == expected_output
