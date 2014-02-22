__author__ = 'paymahnmoghadasian'

import unittest
from testBaseQuicksort import testBaseQuicksort

def main():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testBaseQuicksort))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()