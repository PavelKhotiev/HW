import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_filter_by_currency_rub(sample_transactions):
    rub_transactions = filter_by_currency(sample_transactions, "RUB")
    assert next(rub_transactions)["id"] == 873106923
    assert next(rub_transactions)["id"] == 594226727


def test_filter_by_currency_not_found(sample_transactions):
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(eur_transactions)


def test_filter_by_currency_generator(sample_transactions):
    def transaction_generator():
        for transaction in sample_transactions:
            yield transaction

    usd_transactions = filter_by_currency(transaction_generator(), "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_empty():
    transactions = []
    descriptions = transaction_descriptions(transactions)
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_missing_description(sample_transactions):
    sample_transactions.append({"id": 123456789, "state": "EXECUTED", "date": "2021-01-01T00:00:00.000000"})
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == ""


def test_card_number_generator():
    start = 1
    end = 5
    expected_output = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    generated_output = list(card_number_generator(start, end))

    assert generated_output == expected_output


def test_card_number_generator_single_value():
    start = 1234567890123456
    end = 1234567890123456
    expected_output = ["1234 5678 9012 3456"]

    generated_output = list(card_number_generator(start, end))

    assert generated_output == expected_output


def test_card_number_generator_large_range():
    start = 9999999999999995
    end = 9999999999999999
    expected_output = [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]

    generated_output = list(card_number_generator(start, end))

    assert generated_output == expected_output


def test_card_number_generator_empty_range():
    start = 5
    end = 1
    generated_output = list(card_number_generator(start, end))

    assert generated_output == []


def test_card_number_generator_start_end_equal():
    start = 1000000000000000
    end = 1000000000000000
    expected_output = ["1000 0000 0000 0000"]

    generated_output = list(card_number_generator(start, end))

    assert generated_output == expected_output
