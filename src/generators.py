def filter_by_currency(transactions, currency):
    """принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction
