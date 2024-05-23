from src.masks import card_mask, number_account_mask


def mask_card_or_account(input_str: str) -> str:
    """Функция  принимает на вход строку нужного формата
    или для маскировки и используются функции из модуля masks"""
    if "Счет" in input_str:
        return f"Счет {number_account_mask(input_str.split()[-1])}"
    else:
        card_number = input_str.split()[-1]
        masked_card = card_mask(card_number)
        if masked_card == "Неверный номер карты":
            return "Неверный номер карты"
        else:
            return " ".join(input_str.split()[:-1]) + " " + masked_card


# def format_date(date_str: str) -> str:
#     """Ф-ция, которая принимает на вход строку вида
#     2018-07-11T02:26:18.671407
#     и возвращает строку с датой в виде:
#     11.07.2018."""
#     year = date_str[:4]
#     month = date_str[5:7]
#     day = date_str[8:10]
#
#     formatted_date = f"{day}.{month}.{year}"
#     return formatted_date


def format_date(date_str: str) -> str:
    """Ф-ция, которая принимает на вход строку вида
    2018-07-11T02:26:18.671407 и возвращает строку с датой в виде: 11.07.2018.
    Если дата невалидна, возвращает 'Неверный формат даты'."""
    if len(date_str) != 26 or date_str[10] != 'T':
        return 'Неверный формат даты'

    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return 'Неверный формат даты'

    year = int(year)
    month = int(month)
    day = int(day)

    if not (1 <= month <= 12):
        return 'Неверный формат даты'

    days_in_month = [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31,
                     30, 31, 30, 31]

    if not (1 <= day <= days_in_month[month - 1]):
        return 'Неверный формат даты'

    formatted_date = f"{day:02}.{month:02}.{year}"
    return formatted_date

#  Решение нашел в гугле, т.к. неясно как еще изменить изначальную ф-цию, чтобы тесты проходили
