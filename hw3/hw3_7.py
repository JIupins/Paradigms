class SortStrategy:
    def sort(self, numbers):
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, numbers):
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


class SelectionSortStrategy(SortStrategy):
    def sort(self, numbers):
        for i in range(len(numbers)):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_numbers(self, numbers):
        self.strategy.sort(numbers)


sorter = Sorter(BubbleSortStrategy())

numbers = [5, 2, 8, 1, 9]
sorter.sort_numbers(numbers)
print(numbers)

sorter.set_strategy(SelectionSortStrategy())
sorter.sort_numbers(numbers)
print(numbers)