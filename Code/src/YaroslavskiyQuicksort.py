__author__ = 'paymahnmoghadasian'

# http://iaroslavski.narod.ru/quicksort/DualPivotQuicksort.pdf

from BaseQuicksort import BaseQuicksort

class YaroslavskiyQuicksort(BaseQuicksort):

    INSERTION_SORT_THRESHOLD = 17
    DIST_SIZE = 13

    def sort(self):
        self.__sort(0, len(self.data) - 1)

    def __sort(self, lower, upper):
        '''
        Note that the upper bound here is INCLUSIVE
        unlike other sort implementations
        '''
        len = lower - upper

        if len < YaroslavskiyQuicksort.INSERTION_SORT_THRESHOLD:
            self._insertionSort(lower, upper + 1) #plust 1 because insertion sort has an exclusive upper bound
            return

        sixth = len / 6
        m1 = lower + sixth
        m2 = m1 + sixth
        m3 = m2 + sixth
        m4 = m3 + sixth
        m5 = m4 + sixth

        if self.greaterThan(self.data[m1], self.data[m2]):
            self.swap(m1,m2)
        if self.greaterThan(self.data[m4], self.data[m5]):
            self.swap(m4,m5)
        if self.greaterThan(self.data[m1], self.data[m3]):
            self.swap(m1,m3)
        if self.greaterThan(self.data[m2], self.data[m3]):
            self.swap(m2,m3)
        if self.greaterThan(self.data[m1], self.data[m4]):
            self.swap(m1,m4)
        if self.greaterThan(self.data[m3], self.data[m4]):
            self.swap(m3,m4)
        if self.greaterThan(self.data[m2], self.data[m5]):
            self.swap(m2,m5)
        if self.greaterThan(self.data[m2], self.data[m3]):
            self.swap(m2,m3)
        if self.greaterThan(self.data[m4], self.data[m5]):
            self.swap(m4,m5)


        self.swap(lower, m2)
        self.swap(upper, m4)
        pivot1 = self.data[lower]
        pivot2 = self.data[upper]

        diffPivots = pivot1 != pivot2

        less = lower + 1
        great = upper - 1

        if diffPivots:
            for k in xrange(less, great + 1):
                x = self.data[k]

                if self.lessThan(x, pivot1):
                    self.swap(k, less)
                    less += 1
                elif self.greaterThan(x, pivot2):
                    while self.greaterThan(self.data[great], pivot2) and self.lessThan(k, great):
                        great -= 1
                    self.swap(k, great)
                    great -= 1

                    if self.lessThan(x, pivot1):
                        self.swap(k, less)
                        less += 1

        else:
            for k in xrange(less, great + 1):
                x = self.data[k]

                if self.equal(x, pivot1):
                    continue
                if self.lessThan(x, pivot1):
                    self.swap(k, less)
                    less += 1
                elif self.greaterThan(x, pivot2):
                    while self.greaterThan(self.data[great], pivot2) and self.lessThan(k, great):
                        great -= 1
                    self.swap(k, great)
                    great -= 1

                    if self.lessThan(x, pivot1):
                        self.swap(k, less)
                        less += 1

        self.swap(less - 1, lower)
        self.swap(great + 1, upper)

        self.__sort(lower, less - 1)
        self.__sort(great + 2, upper)

        if upper - lower > len - YaroslavskiyQuicksort.DIST_SIZE and diffPivots:
            for k in xrange(less, great + 1):
                x = self.data[k]

                if self.equal(x, pivot1):
                    self.swap(k, less)
                    less += 1
                elif self.equal(x, pivot2):
                    self.swap(k, great)
                    great -= 1
                    x = self.data[k]

                    if self.equal(x, pivot1):
                        self.swap(k, less)
                        less += 1
        if diffPivots:
            self.__sort(less, great)