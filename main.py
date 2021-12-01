from arrange import ArrangeRandom, ArrangeByAsc, ArrangeByDesc, ArrangeReverse
from sorting import Results, BubbleSort, SelectionSort


def printAndSelectAlgorithms(structure: dict, inputMessage: str) -> list[str]:
    for key, value in structure.items():
        print("> ", key, "\n")

    print(inputMessage)
    selOptions = input()

    return selOptions.split(" ")


def getAlgorithmsByName(structure: dict, listOfNames: list[str]) -> list:
    selectedAlgorithms: list = []

    for name in listOfNames:
        selectedAlgorithms.append(structure[name])

    return selectedAlgorithms


def chooseAlgorithms(algorithms: dict, inputMsg: str) -> list:
    names: list[str] = printAndSelectAlgorithms(algorithms, inputMsg)
    algorithms: list = getAlgorithmsByName(algorithms, names)

    return algorithms


def executeSelectedAlgorithms(selectedAlgorithms: list, arr: list, execution):
    results: list = []

    for algo in selectedAlgorithms:
        result = getattr(algo, execution)(arr)
        results.append(result)

    return results


def chooseAndExecuteSelectedAlgorithms(allAlgorithms: dict, arr: list, displayMsg: str, execution) -> list:
    selectedAlgorithms: list = chooseAlgorithms(allAlgorithms, displayMsg)
    results: list = executeSelectedAlgorithms(selectedAlgorithms, arr, execution)

    return results


def chooseArrangement(arrangement: list[int]) -> list[int]:
    allArrangements = {
        "Aleatoria": ArrangeRandom(),
        "Crescente": ArrangeByAsc(),
        "Decrescente": ArrangeByDesc(),
        "Invertida": ArrangeReverse()
    }

    displayMsg = "Seu arranjo é: {}\nDigite a formatação que deseja para o arranjo da maneira em que está escrita".format(initialArr)
    arrangements: list[list] = chooseAndExecuteSelectedAlgorithms(allArrangements, arrangement, displayMsg, 'arrange')

    print("Seu arranjo agora é: {}\n".format(arrangements[0]))
    return arrangements[0]


def chooseSorting(arrangement: list[int]) -> list[Results]:
    allSortings = {
        "BubbleSort": BubbleSort(),
        "SelectionSort": SelectionSort(),
    }

    displayMsg = "Digite o nome dos algoritmos que quer selecionar da maneira em que estão escritos, separados APENAS por espaço"
    results: list[Results] = chooseAndExecuteSelectedAlgorithms(allSortings, arrangement, displayMsg, 'sort')
    return results


def printResults(results):
    for result in results:
        result.printResults()


if __name__ == '__main__':

    initialArr = [5, 8, 10, 2, 1, 53, 5, 4, 90, 0]

    arrangement = chooseArrangement(initialArr)
    results = chooseSorting(arrangement)

    printResults(results)









