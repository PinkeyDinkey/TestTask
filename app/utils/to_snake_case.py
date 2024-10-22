"""Модуль утилит для преобразования строк"""

from .constant import SNAKE_CASE_PATTERN


def to_snake_case(camel_str: str) -> str:
    """
    Метод преобразования строки в snake case

    Args:
        camel_str (str): Строка в camel case

    Returns:
        str: Строка в snake case
    """
    return SNAKE_CASE_PATTERN.sub("_", camel_str).lower()
