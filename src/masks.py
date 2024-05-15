def card_mask(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX.
    Т. е. видны первые 6 цифр и последние 4,
    номер разбит по блокам по 4 цифры, разделенным пробелами."""
    number_card_str = str(number_card)
    number_card_str = number_card_str.replace(" ", "")
    masked_number = f"{number_card_str[:4]} {number_card_str[4:6]}** **** {number_card_str[-4:]}"
    return masked_number


def number_account_mask(number_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате"""
    account_str = str(number_account)
    last_digits = account_str[-4:]
    masked_number = "**" + last_digits
    return masked_number
