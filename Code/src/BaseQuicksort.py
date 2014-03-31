__author__ = 'paymahnmoghadasian'


class BaseQuicksort():
    '''
    Base class for the quicksorts that we will implement
    '''
    def __init__(self, data, doInsertionSort = False, insertionSortThreshold=13, pivotSelection=1, numPivots=1):
        self.__numSwaps = 0
        self.__numComparisons = 0
        self.__data = data
        self.__doInsertionSort = doInsertionSort
        self.__insertionSortThreshold = insertionSortThreshold
        self.__pivotSelection = pivotSelection
        self.__numPivots = numPivots

    def __getPivotSelection(self):
        return self.__pivotSelection
    pivotSelection = property(__getPivotSelection)

    def __getNumPivots(self):
        return self.__numPivots
    numPivots = property(__getNumPivots)

    def __getInsertionSortThreshold(self):
        return self.__insertionSortThreshold
    insertionSortThreshold = property(__getInsertionSortThreshold)

    def __getDoInsertionSort(self):
        return self.__doInsertionSort
    doInsertionSort = property(__getDoInsertionSort)

    def getNumSwaps(self):
        return self.__numSwaps
    def setNumSwaps(self, value):
        self.__numSwaps = value
    def delNumSwaps(self):
        del self.__numSwaps
    numSwaps = property(getNumSwaps, setNumSwaps, delNumSwaps, "The number of swaps done by the sort algorithm")

    def getNumComparisons(self):
        return self.__numComparisons
    def setNumComparisons(self, value):
        self.__numComparisons = value
    def delNumComparisons(self):
        del self.__numComparisons
    numComparisons = property(getNumComparisons, setNumComparisons,delNumComparisons, "The number of comparisons done by the sorting algorithm")

    def getData(self):
        return self.__data
    def setData(self, value):
        self.__data = value
    def delData(self):
        del self.__data
    data = property(getData, setData,delData, "The data to be sorted")


    def sort(self):
        raise NotImplementedError("Cannot sort on base quicksort")

    def _insertionSort(self, data, lower, upper):
        '''
        Sorts self.data from [lower,upper) using insertion sort
        Lower is an inclusive bound
        Upper is an exclusive bound
        '''
        for i in xrange(lower + 1, upper):
            j = i
            while j > lower and self.lessThan(data[j],  data[j-1]):
                self.swap(j, j-1)
                j -= 1

        return data

    def lessThan(self, a, b):
        '''
        determines whether a < b
        '''
        self.numComparisons += 1
        return a < b

    def lessThanEqual(self, a, b):
        '''
        determines whether a <= b
        '''
        self.numComparisons += 1
        return a <= b

    def greaterThan(self, a, b):
        '''
        determines whether a > b
        '''
        self.numComparisons += 1
        return a > b

    def greaterThanEqual(self, a, b):
        '''
        determines whether a >= b
        '''
        self.numComparisons += 1
        return a >= b

    def equal(self, a, b):
        '''
        determines whether a == b
        '''
        self.numComparisons += 1
        return a == b

    def swap(self, index1, index2):
        '''
        swaps the data[index1] and data[index2]
        '''
        self.numSwaps += 1
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]