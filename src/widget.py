from src.masks import card_mask, number_account_mask


def mask_card_or_account(input_str: str) -> str:
    """Функция  принимает на вход строку нужного формата
    или для маскировки не используются функции из модуля masks"""
    if "Счет" in input_str:
        return f"Счет {number_account_mask(input_str.split()[-1])}"
    else:
        return " ".join(input_str.split()[:-1]) + " " + card_mask(input_str.split()[-1])


def format_date(date_str: str) -> str:
    """Ф-ция, которая принимает на вход строку вида
    2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде:
    11.07.2018."""
    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]

    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


print(mask_card_or_account("Visa Platinum 8990922113665229"))
