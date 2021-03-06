__author__ = 'paymahnmoghadasian'

# http://iaroslavski.narod.ru/quicksort/DualPivotQuicksort.pdf

from BaseQuicksort import BaseQuicksort

class YaroslavskiyQuicksort(BaseQuicksort):

    INSERTION_SORT_THRESHOLD = 17
    DIST_SIZE = 13

    def __init__(self, data):
        BaseQuicksort.__init__(self, data, True, YaroslavskiyQuicksort.INSERTION_SORT_THRESHOLD, 1, 2)

    def sort(self):
        self.__sort(0, len(self.data) - 1)

    def __sort(self, left, right):
        '''
        Note that the upper bound here is INCLUSIVE
        unlike other sort implementations
        '''
        len = right - left

        if len < YaroslavskiyQuicksort.INSERTION_SORT_THRESHOLD:
            self._insertionSort(self.data, left, right + 1) #plust 1 because insertion sort has an exclusive upper bound
            return

        sixth = len / 6
        m1 = left + sixth
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


        self.swap(m2, left)
        self.swap(m4, right)
        pivot1 = self.data[left]
        pivot2 = self.data[right]

        diffPivots = pivot1 != pivot2

        less = left + 1
        great = right - 1

        if diffPivots:
            k = less
            while k <= great:
                x = self.data[k]

                if self.lessThan(x, pivot1):
                    self.swap(k, less)
                    less += 1
                elif self.greaterThan(x, pivot2):
                    while self.greaterThan(self.data[great], pivot2) and k < great:
                        great -= 1
                    self.swap(k, great)
                    great -= 1
                    x = self.data[k]

                    if self.lessThan(x, pivot1):
                        self.swap(k, less)
                        less += 1

                k += 1

        else:
            k = less
            while k <= great:

                x = self.data[k]

                if self.equal(x, pivot1):
                    continue
                if self.lessThan(x, pivot1):
                    self.swap(k, less)
                    less += 1
                elif self.greaterThan(x, pivot2):
                    while self.greaterThan(self.data[great], pivot2) and k < great:
                        great -= 1
                    self.swap(k, great)
                    great -= 1
                    x = self.data[k]

                    if self.lessThan(x, pivot1):
                        self.swap(k, less)
                        less += 1

                k += 1

        # swap
        self.swap(left, less -1)
        self.swap(right, great + 1)

        #recursive calls
        self.__sort(left, less - 2)
        self.__sort(great + 2, right)

        if great - less > len - YaroslavskiyQuicksort.DIST_SIZE and diffPivots:
            k = less
            while k <= great:

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

                k += 1
        if diffPivots:
            self.__sort(less, great)