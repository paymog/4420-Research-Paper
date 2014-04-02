__author__ = 'paymahnmoghadasian'

from BaseQuicksort import BaseQuicksort


class DualPivotQuicksort(BaseQuicksort):

    def __init__(self, data, doInsertionSort=False, insertionSortThreshold=10, pivotSelection=1, behaveOptimally=False):
        '''
        :param pivotSelection: This determines how pivots are chosen. There are exactly 2 valid values: 1 and 2. 1 is the default where the first and last values in the range are chosen. 2 is where tertiles are chosen.
        '''

        if pivotSelection != 1 and pivotSelection != 2:
            raise ValueError("The value of the pivot selection (%d) is invalid. Must be 1 or 2." % pivotSelection)

        BaseQuicksort.__init__(self, data, doInsertionSort, insertionSortThreshold, pivotSelection, 2)

        self.__behaveOptimally = behaveOptimally

    def sort(self):
        self.__sort(0, len(self.data))

    def __partitionOptimally(self, largePivot, lower, smallPivot, upper):
        lowerSwap = i = lower + 1
        upperSwap = upper - 2
        smallCount = largeCount = 0 # number of elements smaller than the small pivot and larger than the large pivot

        while i <= upperSwap:
            if smallCount >= largeCount:
                if self.lessThan(self.data[i], smallPivot):
                    self.swap(i, lowerSwap)
                    lowerSwap += 1
                    smallCount += 1
                elif self.greaterThan(self.data[i], largePivot):
                    #don't want to swap stuff that's bigger than the largePivot
                    while i < upperSwap and self.greaterThan(self.data[upperSwap], largePivot):
                        upperSwap -= 1

                    self.swap(i, upperSwap)
                    upperSwap -= 1
                    largeCount += 1

                    if self.lessThan(self.data[i], smallPivot):
                        self.swap(i, lowerSwap)
                        lowerSwap += 1
                        smallCount += 1
            else:
                if self.greaterThan(self.data[i], largePivot):
                    #don't want to swap stuff that's bigger than the largePivot
                    while i < upperSwap and self.greaterThan(self.data[upperSwap], largePivot):
                        upperSwap -= 1

                    self.swap(i, upperSwap)
                    upperSwap -= 1
                    largeCount += 1

                    if self.lessThan(self.data[i], smallPivot):
                        self.swap(i, lowerSwap)
                        lowerSwap += 1
                        smallCount += 1

                elif self.lessThan(self.data[i], smallPivot):
                    self.swap(i, lowerSwap)
                    lowerSwap += 1
                    smallCount += 1

            i += 1

        return lowerSwap, upperSwap


    def __partition(self, largePivot, lower, smallPivot, upper):

        lowerSwap = i = lower + 1
        upperSwap = upper - 2

        if self.__behaveOptimally:
            lowerSwap, upperSwap = self.__partitionOptimally(largePivot, lower, smallPivot, upper)
        else:
            while i <= upperSwap:
                if self.lessThan(self.data[i], smallPivot):
                    self.swap(i, lowerSwap)
                    lowerSwap += 1
                elif self.greaterThan(self.data[i], largePivot):
                    #don't want to swap stuff that's bigger than the largePivot
                    while i < upperSwap and self.greaterThan(self.data[upperSwap], largePivot):
                        upperSwap -= 1
                    self.swap(i, upperSwap)
                    upperSwap -= 1

                    if self.lessThan(self.data[i], smallPivot):
                        self.swap(i, lowerSwap)
                        lowerSwap += 1

                i += 1

        return lowerSwap, upperSwap

    def __sort(self, lower, upper):

        #check whether we should do an insertion sort instead of quicksort
        if self.doInsertionSort and upper - lower <= self.insertionSortThreshold:
            self._insertionSort(self.data, lower, upper)
            return

        #base cases
        if upper - lower <= 1:
            return
        if upper - lower == 2:
            if self.lessThan(self.data[upper-1], self.data[lower]):
                self.swap(lower, upper-1)
            return

        # select the pivots. If they're the same, this section is sorted
        smallPivot, largePivot = self.__selectPivots(lower, upper)
        # if self.equal(smallPivot, largePivot):
        #     return

        lowerSwap, upperSwap = self.__partition(largePivot, lower, smallPivot, upper)

        self.swap(lower, lowerSwap - 1)
        self.swap(upper - 1, upperSwap + 1)

        self.__sort(lower, lowerSwap-1)
        self.__sort(lowerSwap, upperSwap+1)
        self.__sort(upperSwap+2, upper)

    def __selectPivots(self, lower, upper):
        '''
        Default pivot selection guarantees that if the pivots can be different, they will be
        Tertiles does NOT make this guarantee
        '''

        # to do tertiles pivot selection, the range must be big enough
        if upper - lower >= 5 and self.pivotSelection == 2:
            middle = lower + (upper - lower) / 2
            left = lower + (middle - lower) / 2
            right = middle + (upper - middle) / 2

            #sort the potential pivot values and keep track of their index
            pivots = [(self.data[lower], lower), (self.data[left], left), (self.data[middle], middle),
                      (self.data[right], right), (self.data[upper - 1], upper - 1)]
            pivots = self._insertionSort(pivots, 0, len(pivots))

            #put the desired pivots at the beginning and end of the range
            self.swap(lower, pivots[1][1])
            if self.equal(lower, pivots[3][1]):
                self.swap(upper - 1, pivots[1][1])
            else:
                self.swap(upper - 1, pivots[3][1])

        else:
            i = lower
            while self.equal(self.data[i], self.data[upper-1]) and i < upper:
                i += 1

            self.swap(i, lower)

            if self.lessThan(self.data[upper - 1], self.data[lower]):
                self.swap(lower, upper - 1)

        return self.data[lower], self.data[upper - 1]