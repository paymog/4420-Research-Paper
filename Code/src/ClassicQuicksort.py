from src.BaseQuicksort import BaseQuicksort

__author__ = 'paymahnmoghadasian'


class ClassicQuicksort(BaseQuicksort):
    def __init__(self, data, doInsertionSort=False, insertionSortThreshold=10):
        BaseQuicksort.__init__(self, data)
        self.doInsertionSort = doInsertionSort
        self.insertionSortThreshold = insertionSortThreshold

    def sort(self):
        self.__sort(0, len(self.data))
        return self.data

    def __sort(self, lower, upper):
        if self.doInsertionSort and upper - lower <= self.insertionSortThreshold:
            self._insertionSort(lower, upper)

        if upper - lower <= 1:
            return
        if upper - lower == 2:

            if self.lessThan(self.data[upper-1], self.data[lower]):
                self.swap(lower, upper-1)
            return

        pivot = self.data[lower]
        i = lower+1
        for j in range(lower, upper):
            if self.lessThan(self.data[j], pivot):
                self.swap(i, j)
                i += 1

        self.swap(lower, i-1)
        self.__sort(lower, i-1)
        self.__sort(i, upper)