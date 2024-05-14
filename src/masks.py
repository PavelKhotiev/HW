def card_mask(number_card: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX.
    Т. е. видны первые 6 цифр и последние 4,
    номер разбит по блокам по 4 цифры, разделенным пробелами."""
    if len(str(number_card)) == 16:
        number_card_str = str(number_card)
        number_card_str = number_card_str.replace(" ", "")
        masked_number = number_card_str[:4] + " " + number_card_str[4:6] + "** **** " + number_card_str[-4:]
        return masked_number
    else:
        return "Некорректный номер карты"


def number_account_mask(number_account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате"""
    if len(str(number_account)) == 20:
        account_str = str(number_account)
        last_digits = account_str[-4:]
        masked_number = "**" + last_digits
        return masked_number
    else:
        return "Введен неверный счет"


print(number_account_mask(73654108430155874305))
