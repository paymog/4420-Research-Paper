__author__ = 'paymahnmoghadasian'

import unittest
from ..src.DualPivotQuicksort import DualPivotQuicksort, PivotSelectionMechanism

class testDualPivotQuicksort(unittest.TestCase):


    def test_DefaultPivot_OneDifferentElement(self):
        self.sort = DualPivotQuicksort(None)

        #other test cases
        self.sort.data = [1,2,1,1]
        self.sort.sort()
        self.assertEqual([1,1,1,2], self.sort.data)

        self.sort.data = [1,1,2,1]
        self.sort.sort()
        self.assertEqual([1,1,1,2], self.sort.data)

        self.sort.data = [2,1,2,2]
        self.sort.sort()
        self.assertEqual([1,2,2,2], self.sort.data)

        self.sort.data = [2,2,1,2]
        self.sort.sort()
        self.assertEqual([1,2,2,2], self.sort.data)


    def test_TertilesPivot(self):
        self.sort = DualPivotQuicksort(None, pivotSelection=PivotSelectionMechanism.Tertiles)
        self.sort.data = [4,1,2,3,5]
        self.sort.sort()
        self.assertEqual([1,2,3,4,5], self.sort.data)


    def test_SelectPivot(self):
        self.sort = DualPivotQuicksort(None)
        self.sort.data = [1, 2]
        self.assertPivots(1,2)
        self.assertEqual([1,2], self.sort.data)

        self.sort.data = [2,1]
        self.assertPivots(1,2)
        self.assertEqual([1,2], self.sort.data)

        self.sort.data = [2,1,2]
        self.assertPivots(1,2)
        self.assertEqual([1,2,2], self.sort.data)

        self.sort.data = [2,3,1,2]
        self.assertPivots(2,3)
        self.assertEqual([2,2,1,3], self.sort.data)

        self.sort.data = [1,1,2,1]
        self.assertPivots(1,2)
        self.assertEqual([1,1,1,2], self.sort.data)

        self.sort.data = [1,2,3,4,5]
        self.assertPivots(1,5)
        self.assertEqual([1,2,3,4,5], self.sort.data)



        self.sort = DualPivotQuicksort(None, pivotSelection=PivotSelectionMechanism.Tertiles)

        # defaults to the defualt selection mechanism when the range isn't big enough
        self.sort.data = [2,3,4,5]
        self.assertPivots(2, 5)
        self.assertEqual([2,3,4,5], self.sort.data)

        self.sort.data = [2,3,4]
        self.assertPivots(2,4)
        self.assertEqual([2,3,4], self.sort.data)

        self.sort.data = [4,1,2,3,5]
        self.assertPivots(2,4)
        self.assertEqual([2,1,5,3,4], self.sort.data)

        self.sort.data = [5,4,3,2,1]
        self.assertPivots(2,4)
        self.assertEqual([2,1,3,5,4], self.sort.data)



    def assertPivots(self, small, large):
        s, l = self.sort._DualPivotQuicksort__selectPivots(0, len(self.sort.data))
        self.assertEqual(small, s)
        self.assertEqual(large, l)