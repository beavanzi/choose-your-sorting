import random
from abc import ABC, abstractmethod

class Arrange(ABC):
    @abstractmethod
    def arrange(self, items: list) -> list:
        pass


class ArrangeRandom(Arrange):
    def arrange(self, items: list) -> list:
        return random.sample(items, len(items))


class ArrangeByAsc(Arrange):
    def arrange(self, items: list) -> list:
        items.sort()
        return items


class ArrangeByDesc(Arrange):
    def arrange(self, items: list) -> list:
        items.sort(reverse=True)
        return items


class ArrangeReverse(Arrange):
    def arrange(self, items: list) -> list:
        items.reverse()
        return items
