__author__ = 'paymahnmoghadasian'

from BaseQuicksort import BaseQuicksort

class DualPivotQuicksort(BaseQuicksort):

    def sort(self):
        self.__sort(0, len(self.data))

    def __sort(self, lower, upper):

        #base cases
        if upper - lower <= 1:
            return
        if upper - lower == 2:
            if self.lessThan(self.data[upper-1], self.data[lower]):
                self.swap(lower, upper-1)
            return

        # select the pivots. If they're the same, this section is sorted
        smallPivot, largePivot = self.__selectPivots(lower, upper)
        if self.equal(smallPivot, largePivot):
            return

        lowerSwap = i = lower + 1
        upperSwap = upper - 2
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

        self.swap(lower, lowerSwap - 1)
        self.swap(upper - 1, upperSwap + 1)

        self.__sort(lower, lowerSwap-1)
        self.__sort(lowerSwap, upperSwap+1)
        self.__sort(upperSwap+2, upper)

    def __selectPivots(self, lower, upper):
        '''
        Attempts to select two different pivots. If the range only has at least two different
        values, this method will guarantee that the two returned values are different
        '''

        i = lower
        while self.equal(self.data[i], self.data[upper-1]) and i < upper:
            i += 1

        self.swap(i, lower)

        if self.lessThan(self.data[upper - 1], self.data[lower]):
            self.swap(lower, upper - 1)

        return self.data[lower], self.data[upper - 1]