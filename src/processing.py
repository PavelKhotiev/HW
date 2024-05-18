def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Ф-ция,  принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение."""
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: list, descending: bool = True) -> list:
    """принимает на вход список словарей и возвращает новый список, в котором
    исходные словари отсортированы по убыванию даты"""

    def get_date(item: dict) -> str:
        return item["date"]

    sorted_data = sorted(data, key=get_date, reverse=descending)
    return sorted_data


# P.S. mypy выдаёт ошибку - не могу исправить, не понимаю что ему не нравится
