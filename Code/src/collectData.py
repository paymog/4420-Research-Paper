__author__ = 'paymahn'

import random
from time import time

from ClassicQuicksort import ClassicQuicksort
from YaroslavskiyQuicksort import YaroslavskiyQuicksort

def generateData(minLength, maxLength, lowerBound, upperBound):
    for i in range(minLength, maxLength):
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

str = "%s,%d,%s,%d,%f,%d,%d\n"
for data in generateData(9999,10000, 0, 1000000):
    dataLength = len(data)

    t = time()
    sorted(list(data))
    print time() - t

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


file.close()