from abc import ABC, abstractmethod
import time
from copy import deepcopy


class Results:
    def __init__(self, algorithmName, items, executionTime):
        self.algorithmName: str = algorithmName
        self.items: list = items
        self.executionTime: str = executionTime

    def getAlgorithmName(self):
        return self.algorithmName

    def getItems(self):
        return self.items

    def getExecutionTime(self):
        return self.executionTime

    def printResults(self):
        msg = "\nAlgoritmo: {} | Resultado: {} | Tempo de execução: {}\n".format(self.getAlgorithmName(), self.getItems(), self.getExecutionTime())
        print(msg)


class SortingAlgorithm(ABC):

    @abstractmethod
    def sort(self, items: list) -> Results:
        pass


class BubbleSort(SortingAlgorithm):

    def sort(self, initialItems: list) -> Results:
        startTime = time.time()

        items = deepcopy(initialItems)
        n = len(items)

        changes = 0
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    changes += 1
                    print("\nTrocas no BubbleSort: ", changes)

        endTime = time.time() - startTime
        return Results("BubbleSort", items, endTime)


class SelectionSort(SortingAlgorithm):

    def sort(self, initialItems: list) -> Results:
        startTime = time.time()

        items = deepcopy(initialItems)
        n = len(items)

        for i in range(n):
            minIndex = i
            for j in range(i+1, n):
                if items[minIndex] > items[j]:
                    minIndex = j

            items[i], items[minIndex] = items[minIndex], items[i]
            print("\nTrocas no SelectionSort: ", i)

        endTime = time.time() - startTime
        return Results("SelectionSort", items, endTime)

