from BaseQuicksort import BaseQuicksort

__author__ = 'paymahnmoghadasian'

class ClassicQuicksort(BaseQuicksort):
    def __init__(self, data, doInsertionSort=False, insertionSortThreshold=10, pivotSelection=1):
        '''
        :param pivotSelection: Determines how the pivot should be chosen. 1 = 1st in range. 2 = last in range. 3 = median of first, middle and last in range.
        '''
        BaseQuicksort.__init__(self, data)
        self.__doInsertionSort = doInsertionSort
        self.__insertionSortThreshold = insertionSortThreshold

        if pivotSelection != 1 and pivotSelection != 2 and pivotSelection != 3:
            raise ValueError("The value of the pivot selection (%d) is invalid. Must be 1 or 2." % self.pivotSelection)

        self.__pivotSelection = pivotSelection

    def __getDoInsertionSort(self):
        return self.__doInsertionSort
    doInsertionSort = property(__getDoInsertionSort)

    def __getInsertionSortThreshold(self):
        return self.__insertionSortThreshold
    insertionSortThreshold = property(__getInsertionSortThreshold)

    def __getPivotSelection(self):
        return self.__pivotSelection
    pivotSelection = property(__getPivotSelection)

    def sort(self):
        self.__sort(0, len(self.data))
        return self.data

    def __sort(self, lower, upper):
        #check whether we should do an insertion sort instead of quicksort
        if self.__doInsertionSort and upper - lower <= self.__insertionSortThreshold:
            self._insertionSort(lower, upper)
            return

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
        for j in xrange(lower+1, upper):
            if self.lessThan(self.data[j], pivot):
                self.swap(i, j)
                i += 1

        #do the recursive calls
        self.swap(lower, i-1)
        self.__sort(lower, i-1)
        self.__sort(i, upper)

    def __selectPivot(self, lower, upper):
        if self.__pivotSelection == 2:
            self.swap(lower, upper-1)
        elif self.__pivotSelection == 3:
            middle = lower + (upper - lower) / 2
            pivots = sorted([(self.data[lower], lower), (self.data[middle], middle), (self.data[upper-1], upper-1)])
            self.swap(lower, pivots[1][1])

        return self.data[lower]

