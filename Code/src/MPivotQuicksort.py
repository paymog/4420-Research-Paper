__author__ = 'paymahn'

from BaseQuicksort import BaseQuicksort



class MPivotQuicksort(BaseQuicksort):

    INSERTION_SORT_THRESHOLD = 13

    def __init__(self, data, numPivots, minHeapOptimization=False):
        BaseQuicksort.__init__(self, data)
        self.__numPivots = numPivots
        self.__minHeapOptimization = minHeapOptimization

    def __getNumPivots(self):
        return self.__numPivots
    numPivots = property(__getNumPivots)

    def sort(self):
        self.__sort(0, len(self.data) - 1)

    def __minHeapify(self, first, last):
        '''
        make self.data[first] to self.data[last] satisfy the min heap property
        :param first: inclusive lower bound on what part of the data should be heapified
        :param last: inclusive upper bound on what part of the data should be heapified
        '''
        diff = last - first + 1
        offset = first
        for i in range(diff):

            leftChildIndex = 2 * i + 1
            rightChildIndex = 2 * i + 2

            hasLeftChild = leftChildIndex < diff
            hasRightChild = rightChildIndex < diff

            if not hasLeftChild:
                # curernt element has no "children". No further elements will either
                break

            minChildIndex = leftChildIndex
            if hasRightChild and self.lessThan(self.data[rightChildIndex + offset], self.data[leftChildIndex + offset]):
                minChildIndex = rightChildIndex

            if self.greaterThan(self.data[i + offset], self.data[minChildIndex + offset]):
                self.swap(i + offset, minChildIndex + offset)



    def __sort(self, first, last):
        if first >= last or first < 0:
            return

        if last - first < MPivotQuicksort.INSERTION_SORT_THRESHOLD:
            self._insertionSort(first, last + 1)
            return

        if self.__minHeapOptimization:
            self.__minHeapify(first, last)

        pivots = self.__choosePivots(first, last)


        pivots = sorted(pivots)
        self._insertionSort(pivots[0]-1, last + 1)

        nextStart = first
        for i, currPivot in enumerate(pivots):
            nextGreater = nextStart
            nextGreater = self.__partition(nextStart, nextGreater, currPivot)
            self.swap(nextGreater, currPivot)
            pivots[i] = nextGreater
            self.swap(nextGreater + 1, currPivot + 1)

            if nextStart == first and pivots[i] > nextStart + 1:
                self.__sort(nextStart, pivots[i] - 1)

            if nextStart != first and pivots[i] > pivots[i-1] + 2:
                self.__sort(pivots[i-1]+1, pivots[i]+1)

            nextStart = nextGreater + 2
        if last > pivots[-1] + 1:
            self.__sort(pivots[-1]+1, last)



    def __choosePivots(self, first, last):
        pivots = range(self.__numPivots)

        size = last - first + 1
        segments = self.__numPivots + 1
        candidate = size / segments - 1

        next = 2
        if candidate >= 2:
            next = candidate + 1

        candidate += first
        for i in range(self.__numPivots):
            pivots[i] = candidate
            candidate += next

        for i in reversed(range(self.__numPivots)):
            self.swap(pivots[i]+1, last)
            last -= 1
            self.swap(pivots[i], last)
            pivots[i] = last
            last -= 1


        return pivots

    def __partition(self, nextStart, nextGreater, curPivot):
        for curUnknown in range(nextStart, curPivot):
            if self.lessThan(self.data[curUnknown], self.data[curPivot]):
                self.swap(curUnknown, nextGreater)
                nextGreater += 1
        return nextGreater