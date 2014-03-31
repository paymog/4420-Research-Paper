__author__ = 'paymahn'

from BaseQuicksort import BaseQuicksort


class ThreePivotQuicksort(BaseQuicksort):

    def __init__(self, data, doInsertionSort=False, insertionSortThreshold=13, ):
        BaseQuicksort.__init__(self, data, doInsertionSort, insertionSortThreshold, 1, 3)

    def sort(self):
        self.__sort(0, len(self.data)-1)

    def __sort(self, left, right):

        if self.doInsertionSort and right - left < self.insertionSortThreshold:
            self.data = self._insertionSort(self.data, left, right+1)
            return

        smallPivot, middlePivot, largePivot  = self.__selectPivots(left, right)

        a,b,c,d = self.__partition(smallPivot, middlePivot, largePivot, left, right)

        self.__sort(left, a-1)
        self.__sort(a+1, b-1)
        self.__sort(b+1, d-1)
        self.__sort(d+1,right)

    def __partition(self, smallPivot, middlePivot, largePivot, left, right):
        a = b = left + 2
        c = d = right - 1

        while self.lessThanEqual(b,c):
            while self.lessThan(self.data[b], middlePivot) and self.lessThanEqual(b, c):
                if self.lessThan(self.data[b], smallPivot):
                    self.swap(a,b)
                    a += 1
                b += 1
            while self.greaterThan(self.data[c], middlePivot) and self.lessThanEqual(b,c):
                if self.greaterThan(self.data[c], largePivot):
                    self.swap(c,d)
                    d -= 1
                c -= 1
            if self.lessThanEqual(b, c):
                if self.greaterThan(self.data[b], largePivot):
                    if self.lessThan(self.data[c], smallPivot):
                        self.swap(b,a)
                        self.swap(a,c)
                        a += 1
                    else:
                        self.swap(b,c)
                    self.swap(c,d)
                    b += 1
                    c -= 1
                    d -= 1
                else:
                    if self.lessThan(self.data[c], smallPivot):
                        self.swap(b,a)
                        self.swap(a,c)
                        a += 1
                    else:
                        self.swap(b,c)
                    b += 1
                    c -= 1

        a -= 1
        b -= 1
        c += 1
        d += 1
        self.swap(left + 1, a)
        self.swap(a,b)
        a -= 1
        self.swap(left, a)
        self.swap(right,d)

        return a,b,c,d

    def __movePivots(self, pivots, lower, upper):
        '''
        both bounds are inclusive
        moves pivots[0] to lower, pivots[1] to lower + 1 and pivots[2] to upper

        '''
        pivotIndices = [pivot[1] for pivot in pivots]

        currPivot = pivotIndices[0]
        self.swap(lower, currPivot)

        # if one the remaining pivots was previously located at lower, it's now located at currPivot
        pivotIndices = [currPivot if index == lower else index for index in pivotIndices[1:]]

        currPivot = pivotIndices[0]
        self.swap(lower + 1, currPivot)

        # if one the remaining pivots was previously located at lower+1, it's now located at currPivot
        pivotIndices = [currPivot if index == lower+1 else index for index in  pivotIndices[1:]]

        currPivot = pivotIndices[0]
        self.swap(currPivot, upper)





    def __selectPivots(self, lower, upper):
        '''
        returns the indices of the 3 pivots we want to choose
        '''
        diff = upper - lower
        jump = diff / 6
        if jump < 1:
            raise ValueError("Cannot select pivots on a range less than 7 values wide")

        if diff % 6 != 0:
            upper -= diff % 6

        potentialPivots = []

        for i in range(lower, upper+1, jump):
            potentialPivots.append((self.data[i], i))

        if len(potentialPivots) != 7:
            raise RuntimeError("Shit broke. We expected 7 potential pivots")

        potentialPivots = self._insertionSort(potentialPivots, 0, 7)

        pivots = [potentialPivots[1], potentialPivots[3], potentialPivots[5]]
        self.__movePivots(pivots, lower, upper + diff % 6) # + diff % 6 because we subtract that about 10 lines higher

        return [pivot[0] for pivot in pivots] #return the actual pivot values