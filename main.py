import random


class SequenceOptions:
    def __init__(self):
        self.listOfOptions: list = ["aleatoria", "invertida", "crescente", "decrescente"]

    def printOptions(self):
        for (index, entry) in enumerate(self.listOfOptions):
            print(index, "-", entry, "\n")

    def getSequenceByIndex(self, index):
        return self.listOfOptions[index]


class Arrangement:
    def __init__(self, items: list):
        self.items: list = items

    def getItems(self):
        return self.items

    def setInverted(self):
        self.items.reverse()

    def setSortByAsc(self):
        self.items.sort()

    def setSortByDesc(self):
        self.items.sort(reverse=True)

    def setRandom(self):
        self.items = random.sample(self.items, len(self.items))


def getOptions(sequence):
    sequence.printOptions()

    print("q - Sair\n")


def getMenu():
    sequence = SequenceOptions()

    getOptions(sequence)

    arrangement = Arrangement([5, 8, 10, 2, 1, 53, 5, 4, 90, 0])

    selection = input("Selecione a ordem do arranjo:")

    while selection != 'q':
        if selection == :
            print()
        elif selection == '2':
            print(selection)
        elif selection == '3':
            print(selection)
        elif selection == '4':
            print(selection)
        else:
            print("Opção Inválida!")
        selection = input("Selecione a ordem do arranjo:")


if __name__ == '__main__':
    getMenu()
