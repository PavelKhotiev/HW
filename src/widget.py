def mask_card_or_account(user_data: str) -> str:
    """Ф-ция принимает на вход строку с информацией
    — тип карты/счета и номер карты/счета.
    и возвращает исходную строку с
    замаскированным номером карты/счета."""

    divide = user_data.split(" ", 1)
    card_type = divide[0]
    card_number = divide[1]

    if card_type.lower() == "счет":
        masked_number = f"**{card_number[-4:]}"
    else:
        masked_number = f"{card_number[:6]}** **{card_number[-4:]}"

    return f"{card_type} {masked_number}"


def format_date(date_str: str) -> str:
    """Ф-ция, которая принимает на вход строку вида
    2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде
    11.07.2018."""
    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]

    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


print(format_date("2024-05-14T02:26:18.671407"))
