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


def runTests():
    list1 = [5, 8, 10, 2, 1, 53, 5, 4, 90, 0]
    list2 = [0, 90, 4, 5, 53, 1, 2, 10, 8, 5]
    list3 = [90, 53, 1, 5, 0, 10, 8, 4, 2, 5]
    list4 = []
    list5 = []
