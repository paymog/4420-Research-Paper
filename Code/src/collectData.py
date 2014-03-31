__author__ = 'paymahn'

import random
from time import time
import os
import argparse

from multiprocessing.dummy import Pool as ThreadPool

from ClassicQuicksort import ClassicQuicksort
from YaroslavskiyQuicksort import YaroslavskiyQuicksort
from DualPivotQuicksort import DualPivotQuicksort


def mrange(lower, upper, power=2):
    i = lower
    yield int(i)
    while i*power < upper:
        i = i*power
        yield int(i)
    return

def generateData(minLength, maxLength, lowerBound, upperBound):
    for i in mrange(minLength, maxLength, 9./7.):
        data = [random.randint(lowerBound, upperBound) for _ in range(i)]
        yield data

    return

def timeSort(sorter):
    start = time()
    sorter.sort()
    return time() - start

def getUnusedFileName(fileName):
    '''
    Assumes that fileName has a 3 character extension such as 'csv'
    '''
    originalFileName = fileName
    i = 1
    while fileName in os.listdir(os.curdir):
        fileName = originalFileName[:-4] + str(i) + originalFileName[-4:]
        i+= 1

    return fileName

def sortData(data):
    fileName = 'data' + str(len(data)) + '.csv'

    file = open(fileName, 'w')

    # write the header
    file.write("%s,%s,%s,%s,%s,%s,%s\n" % ("Name", "Length", "Used Insertion Sort", "Insertion Sort Threshold", "Time", "Comparisons", "Swaps"))
    asddfsd = "%s,%d,%s,%d,%f,%d,%d\n"

    dataLength = len(data)
    print dataLength

    sorter = ClassicQuicksort(list(data))
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = ClassicQuicksort(list(data), True)
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = ClassicQuicksort(list(data), True, 17)
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = YaroslavskiyQuicksort(list(data))
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('YaroslavskiyQuicksort', dataLength, True, YaroslavskiyQuicksort.INSERTION_SORT_THRESHOLD, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = DualPivotQuicksort(list(data))
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('DualPivot', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = DualPivotQuicksort(list(data), doInsertionSort=True)
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('DualPivot', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = DualPivotQuicksort(list(data), behaveOptimally=True)
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('OptimalDualPivot', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    sorter = DualPivotQuicksort(list(data),doInsertionSort=True, behaveOptimally=True)
    sortTime = timeSort(sorter)
    file.write(asddfsd % ('OptimalDualPivot', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
    file.flush()

    file.close()

def run(minLength, maxLength, lowerRange, upperRange):

    pool = ThreadPool(4)

    data = []
    for a in generateData(minLength, maxLength, lowerRange, upperRange):
        # print a
        data.append(a)

    results = pool.map(sortData, data)

    pool.close()
    pool.join()

    print results

def processDataFiles():

    dataFiles = [a for a in os.listdir(os.curdir) if 'data' in a and '.csv' in a]

    with open('data.csv', 'w') as outfile:
        for fname in dataFiles:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    for fname in dataFiles:
        os.remove(fname)


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-min", "--minLength", type=int, default=4, help="The smallest list length that should be sorted. Default 2.")
    parser.add_argument("-max", "--maxLength", type=int, default=1e8, help="The largest list length that should be sorted. Default 1e8.")
    parser.add_argument("-lr", "--lowerRange", type=int, default=0, help="The smallest value in the list. Default 0.")
    parser.add_argument("-ur", "--upperRange", type=int, default=1e9, help="The largest value in the list. Default 1e9.")

    return parser.parse_args()

if __name__ == '__main__':
    args = getArgs()

    run(args.minLength, args.maxLength, args.lowerRange, args.upperRange)

    processDataFiles()