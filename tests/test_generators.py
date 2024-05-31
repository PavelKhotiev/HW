import pytest

from src.generators import filter_by_currency, transaction_descriptions


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
