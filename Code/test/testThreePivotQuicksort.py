__author__ = 'paymahn'

import unittest
from ..src.ThreePivotQuicksort import ThreePivotQuicksort

class testThreePivotQuicksort(unittest.TestCase):

    def assertPivots(self, small, middle, large, lower, upper):
        s, m, l = self.sort._ThreePivotQuicksort__selectPivots(lower, upper)
        self.assertEqual(small, s)
        self.assertEqual(large, l)
        self.assertEqual(middle, m)


    def test_SelectPivots(self):
        self.sort = ThreePivotQuicksort(None)


        data = range(7)
        self.sort.data = list(data)
        self.assertPivots(1,3,5, 0, len(data) - 1)
        self.assertEqual([1,3,2,0,4,6,5], self.sort.data)

        # all of the pivots are out of place. Should get same result as above
        data = [3,5,2,0,4,6,1]
        self.sort.data = list(data)
        self.assertPivots(1,3,5, 0, len(data) - 1)
        self.assertEqual([1,3,2,0,4,6,5], self.sort.data)


        # put some extra crap at front
        data = [1,2,3,3,5,2,0,4,6,1]
        self.sort.data = list(data)
        self.assertPivots(1,3,5, 3, len(data) - 1)
        self.assertEqual([1,2,3,1,3,2,0,4,6,5], self.sort.data)

        # put some extra crap at end
        data = [3,5,2,0,4,6,1,7,87,9]
        self.sort.data = list(data)
        self.assertPivots(1,3,5, 0, 6)
        self.assertEqual([1,3,2,0,4,6,5, 7,87,9], self.sort.data)

        # put some extra crap on both sides
        data = [-3,-6,3,5,2,0,4,6,1,7,87,9]
        self.sort.data = list(data)
        self.assertPivots(1,3,5, 2, 8)
        self.assertEqual([-3,-6,1,3,2,0,4,6,5, 7,87,9], self.sort.data)

