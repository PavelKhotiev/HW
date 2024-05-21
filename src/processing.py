def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Ф-ция,  принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение."""
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """принимает на вход список словарей и возвращает новый список, в котором
    исходные словари отсортированы по убыванию даты"""

    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list


