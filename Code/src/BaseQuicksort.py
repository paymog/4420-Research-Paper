__author__ = 'paymahnmoghadasian'


class BaseQuicksort():
    '''
    Base class for the quicksorts that we will implement
    '''
    def __init__(self, data):
        self.numSwaps = 0
        self.numComparisons = 0
        self.data = data

    def sort(self):
        raise NotImplementedError("Cannot sort on base quicksort")

    def _insertionSort(self, lower, upper):
        '''
        Sorts self.data from [lower,upper) using insertion sort
        Lower is an inclusive bound
        Upper is an exclusive bound
        '''
        for i in range(lower + 1, upper):
            j = i
            while j > lower and self.lessThan(self.data[j], self.data[j-1]):
                self.swap(j, j-1)
                j -= 1

        return self.data

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