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


