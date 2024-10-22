"""Модуль вспомогательных методов настроек"""

from .constant import MAP


def str_to_bool(value: str) -> bool:
    """
    Метод преобразования строкового представления булевого значения в соответствующее булевое значение

    Args:
        value (str): Строковое представление булевого значения

    Returns:
        bool: Соответствующее булевое значение
    """
    value = str(value).lower()

    if value in MAP:
        return MAP[value]

    raise ValueError(f'"{value}" is not a valid bool value')
