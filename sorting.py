from abc import ABC, abstractmethod


class Results:
    def __init__(self, items, time):
        self.items: list = items
        self.executionTime: str = time

    def getItems(self):
        return self.items

    def getExecutionTime(self):
        return self.executionTime


class SortingAlgorithm(ABC):

    @abstractmethod
    def sort(self, items: list) -> Results:
        pass


class BubbleSort(SortingAlgorithm):

    def sort(self, items: list) -> Results:
        items.sort()
        return Results(items, 'teste1')


class InsertionSort(SortingAlgorithm):

    def sort(self, items: list) -> Results:
        items.sort()
        return Results(items, 'teste2')
