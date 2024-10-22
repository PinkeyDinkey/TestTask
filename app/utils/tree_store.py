"""Модуль объекта TreeStore для построения кастомной иерархичной структуры"""

from itertools import groupby
from typing import Any, Callable, Generator, Iterable, List, Optional


class TreeStore:
    """Объект для построения кастомной иерархичной структуры"""

    def __init__(self, initial_data: Iterable[Any], parent_attr_name: str):
        self.initial_data = initial_data
        self.parent_attr_name = parent_attr_name
        self.data = {item.row_id: item for item in self.initial_data}
        self.parent_child_mapper = {
            parent_id: [item.row_id for item in items]
            for parent_id, items in groupby(
                sorted(
                    self.initial_data,
                    key=lambda x: getattr(x, parent_attr_name) if getattr(x, parent_attr_name) else -1,
                ),
                lambda x: getattr(x, parent_attr_name),
            )
        }

    def get_item(self, row_id: Any) -> Optional[Any]:
        """
        Получение объекта из структуры по параметру

        Args:
            row_id (Any): Параметр, который служит идентификатором элемента

        Returns:
            Optional[Any]: Объект TreeStore
        """
        return self.data.get(row_id)

    def get_children(self, row_id: Any) -> List[Any]:
        """
        Получение списка дочерних объектов по параметру из структуры TreeStore

        Args:
            row_id (Any): Параметр, который служит идентификатором родительского элемента

        Returns:
            List[Any]: Список дочерних элементов
        """
        children_ids = self.parent_child_mapper.get(row_id, [])
        return [self.get_item(child_id) for child_id in children_ids]

    def get_all_parents(self, row_id: Any, parent_attr_name: str) -> List[Any]:
        """
        Получение списка родительских объектов из структуры TreeStore

        Args:
            row_id (Any): Параметр, который служит идентификатором дочернего элемента
            parent_attr_name (str): Наименование параметра, по которому можно получить родительский объект

        Returns:
            List[Any]: Список родительских объектов из структуры TreeStore
        """
        item = self.get_item(row_id) or {}
        if item:
            parent_id = getattr(item, parent_attr_name)
            if parent_id is not None:
                parent = self.get_item(parent_id)
                return [parent] + self.get_all_parents(row_id=parent_id, parent_attr_name=parent_attr_name)
            return []
        return []

    def _build_subtree(self, root: Any, result: List[Any], pred: Callable[[Any], bool]) -> bool:
        """
        Вспомогательный метод для построения поддерева. Добавляет в result вершины, для которых
        выполняется pred, и все их родительские вершины до корня

        Args:
            root (Any): Корневая вершина
            result (List[Any]): Список добавляемых вершин
            pred (Callable[[Any], bool]): Функция-условие для проверки вершин

        Returns:
            bool: True, Если добавлена корневая вершина
        """
        subtree = [self._build_subtree(child, result, pred) for child in self.get_children(root.row_id)]
        if any(subtree) or pred(root):
            result.append(root)
            return True
        return False

    def get_subtree(self, pred: Callable[[Any], bool]) -> "TreeStore":
        """
        Создание поддерева из вершин, для которых выполняется условие, или они входят в путь от корня
        дерева до таких вершин

        Args:
            pred (Callable[[Any], bool]): Функция-условие для проверки вершин

        Returns:
            "TreeStore": Созданное поддерево
        """
        roots = self.get_children(None)
        result = []
        for root in roots:
            self._build_subtree(root, result, pred)
        return TreeStore(result, self.parent_attr_name)

    def get_lower_children(self, row_id: Any) -> List[Any]:
        """
        Получение дочерних элементов на самом нижнем уровне

        Args:
            row_id (Any): Параметр, который служит идентификатором родительского элемента

        Returns:
            List[Any]: Список дочерних элементов
        """
        result = []
        children_ids = self.parent_child_mapper.get(row_id, [])
        for child_id in children_ids:
            child_ids = self.get_lower_children(child_id)
            result.extend(child_ids)
        result.extend(children_ids)
        return result

    def pre_order_traversal(self, row_id: Any = None) -> Generator[Any | None, Any, None]:
        """
        Метод генератора для прямого обхода дерева

        Args:
            row_id (Any): Идентификатором текущего элемента

        Returns:
            Generator[Any | None, Any, None]: Генератор элементов дерева
        """
        if row_id is None:
            for root in self.get_children(None):
                yield from self.pre_order_traversal(root.row_id)
        else:
            if item := self.get_item(row_id):
                yield item
                for child in self.get_children(row_id):
                    yield from self.pre_order_traversal(child.row_id)
