from src.BaseQuicksort import BaseQuicksort
from enum import Enum

__author__ = 'paymahnmoghadasian'

class PivotSelectionMechanism(Enum):
    First = 1,
    Last = 2,
    Median = 3 #takes the median for the first, middle and last elements

class ClassicQuicksort(BaseQuicksort):
    def __init__(self, data, doInsertionSort=False, insertionSortThreshold=10, pivotSelection=PivotSelectionMechanism.First):
        BaseQuicksort.__init__(self, data)
        self.__doInsertionSort = doInsertionSort
        self.__insertionSortThreshold = insertionSortThreshold
        self.__pivotSelection = pivotSelection

    def sort(self):
        self.__sort(0, len(self.data))
        return self.data

    def __sort(self, lower, upper):
        #check whether we should do an insertion sort instead of quicksort
        if self.__doInsertionSort and upper - lower <= self.__insertionSortThreshold:
            self._insertionSort(lower, upper)

        #base cases
        if upper - lower <= 1:
            return
        if upper - lower == 2:
            if self.lessThan(self.data[upper-1], self.data[lower]):
                self.swap(lower, upper-1)
            return

        # recursive case
        pivot = self.__selectPivot(lower, upper)
        i = lower+1
        for j in range(lower+1, upper):
            if self.lessThan(self.data[j], pivot):
                self.swap(i, j)
                i += 1

        #do the recursive calls
        self.swap(lower, i-1)
        self.__sort(lower, i-1)
        self.__sort(i, upper)

    def __selectPivot(self, lower, upper):
        if self.__pivotSelection == PivotSelectionMechanism.Last:
            self.swap(lower, upper-1)
        elif self.__pivotSelection == PivotSelectionMechanism.Median:
            middle = lower + (upper - lower) / 2
            pivots = sorted([(self.data[lower], lower), (self.data[middle], middle), (self.data[upper-1], upper-1)])
            self.swap(lower, pivots[1][1])

        return self.data[lower]

