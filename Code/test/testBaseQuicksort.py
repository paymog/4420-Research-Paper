__author__ = 'paymahnmoghadasian'

import unittest
from ..src.BaseQuicksort import BaseQuicksort

class testBaseQuicksort(unittest.TestCase):
    def setUp(self):
        data = [1,2]
        self.qsort = BaseQuicksort(data)

    def test_lessThan(self):
        self.assertTrue(self.qsort.lessThan(1,2))

