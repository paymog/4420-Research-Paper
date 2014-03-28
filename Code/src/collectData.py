__author__ = 'paymahn'

import random
from time import time
import math

from ClassicQuicksort import ClassicQuicksort
from YaroslavskiyQuicksort import YaroslavskiyQuicksort
from DualPivotQuicksort import DualPivotQuicksort


def mrange(lower, upper, power=2):
    i = lower
    yield int(i)
    while i < upper:
        i = i*power
        yield int(i)
    return

def generateData(minLength, maxLength, lowerBound, upperBound):
    for i in mrange(minLength, maxLength, 9./4.):
        data = [random.randint(lowerBound, upperBound) for _ in range(i)]
        yield data

    return

def timeSort(sorter):
    start = time()
    sorter.sort()
    return time() - start

fileName = 'data.csv'
file = open(fileName, 'w')

headers = ("Name", "Length", "Used Insertion Sort", "Insertion Sort Threshold", "Time", "Comparisons", "Swaps")

file.write("%s,%s,%s,%s,%s,%s,%s\n" % headers)
file.close()

str = "%s,%d,%s,%d,%f,%d,%d\n"
for data in generateData(2,1000000, 0, 1e8):
    file = open(fileName, 'a')

    dataLength = len(data)
    print dataLength

    sorter = ClassicQuicksort(list(data))
    sortTime = timeSort(sorter)
    file.write(str % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))

    sorter = ClassicQuicksort(list(data), True)
    sortTime = timeSort(sorter)
    file.write(str % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))

    sorter = ClassicQuicksort(list(data), True, 17)
    sortTime = timeSort(sorter)
    file.write(str % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))

    sorter = YaroslavskiyQuicksort(list(data))
    sortTime = timeSort(sorter)
    file.write(str % ('YaroslavskiyQuicksort', dataLength, True, YaroslavskiyQuicksort.INSERTION_SORT_THRESHOLD, sortTime, sorter.numComparisons, sorter.numSwaps))

    sorter = DualPivotQuicksort(list(data))
    sortTime = timeSort(sorter)
    file.write(str % ('DualPivot', dataLength, False, -1, sortTime, sorter.numComparisons, sorter.numSwaps))

    sorter = DualPivotQuicksort(list(data), behaveOptimally=True)
    sortTime = timeSort(sorter)
    file.write(str % ('OptimalDualPivot', dataLength, False, -1, sortTime, sorter.numComparisons, sorter.numSwaps))


    file.close()

file.close()