__author__ = 'paymahn'

from ..quicksorts.MPivotQuicksort import MPivotQuicksort
import unittest

class testMPivotQuicksort(unittest.TestCase):

    def assertHeapified(self, lower, upper):
        '''
        exclusive bounds
        '''
        diff = lower - upper + 1
        offset = lower
        for i in range(diff):

            leftChildIndex = 2 * i + 1
            rightChildIndex = 2 * i + 2

            hasLeftChild = leftChildIndex <= diff
            hasRightChild = rightChildIndex <= diff

            if not hasLeftChild:
                # curernt element has no "children". No further elements will either
                break

            if hasLeftChild:
                self.assertTrue(self.sorter.data[i + offset] <= self.sorter.data[leftChildIndex + offset])
            if hasRightChild:
                self.assertTrue(self.sorter.data[i + offset] <= self.sorter.data[rightChildIndex + offset])

    def testHeapify(self):
        self.sorter = MPivotQuicksort(None, 1)
        self.sorter.data = [3,2,1]
        self.heapify(0,len(self.sorter.data))
        self.assertEqual([1,2,3], self.sorter.data)

        self.sorter.data = [3,1,3,2,1]
        self.heapify(2, len(self.sorter.data))
        self.assertEqual([3,1,1,2,3], self.sorter.data)

        self.sorter.data = [3,1,3,2,1,5,4,7,6]
        self.heapify(2, 5)
        self.assertEqual([3,1,1,2,3,5,4,7,6], self.sorter.data)

        self.sorter.data = [3,1,3,2,1,5,4,7,6]
        self.heapify(0, 5)
        self.assertEqual([1,1,3,2,3,5,4,7,6], self.sorter.data)

        self.sorter.data = range(8)[::-1]
        self.heapify(0, len(self.sorter.data))

        self.sorter.data = range(13)[::-1]
        self.heapify(0, len(self.sorter.data))

    def heapify(self, lower, upper):
        '''
        exclusive bounds
        '''
        self.sorter._MPivotQuicksort__minHeapify(lower, upper-1)
        self.assertHeapified(lower, upper)
