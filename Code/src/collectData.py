__author__ = 'paymahn'

import random
from time import time
import os
import argparse
import re

from multiprocessing.dummy import Pool as ThreadPool

from ClassicQuicksort import ClassicQuicksort
from YaroslavskiyQuicksort import YaroslavskiyQuicksort
from DualPivotQuicksort import DualPivotQuicksort
from ThreePivotQuicksort import ThreePivotQuicksort
from MPivotQuicksort import MPivotQuicksort


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

def collectDataForSort(sorter, sorterName, file, dataLength):
    sortTime = timeSort(sorter)
    file.write("%s,%d,%d,%d,%s,%d,%f,%d,%d\n" % (sorterName, dataLength, sorter.pivotSelection, sorter.numPivots,
                                                 sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime,
                                                 sorter.numComparisons, sorter.numSwaps))
    file.flush()

def collectDataForClassicQuicksort(data, file, dataLength):

    ############## FIRST PIVOT SELECTION ################
    sorter = ClassicQuicksort(list(data))
    collectDataForSort(sorter, 'ClassicQuicksort', file, dataLength)

    sorter = ClassicQuicksort(list(data), doInsertionSort=True, insertionSortThreshold=17, pivotSelection=1)
    collectDataForSort(sorter, 'ClassicQuicksort', file, dataLength)

    ############## LAST PIVOT SELECTION ################
    sorter = ClassicQuicksort(list(data), pivotSelection=2)
    collectDataForSort(sorter, 'ClassicQuicksort', file, dataLength)

    sorter = ClassicQuicksort(list(data), doInsertionSort=True, insertionSortThreshold=17, pivotSelection=2)
    collectDataForSort(sorter, 'ClassicQuicksort', file, dataLength)

    ############## MEDIAN PIVOT SELECTION ################
    sorter = ClassicQuicksort(list(data), pivotSelection=3)
    collectDataForSort(sorter, 'ClassicQuicksort', file, dataLength)

    sorter = ClassicQuicksort(list(data), doInsertionSort=True, insertionSortThreshold=17, pivotSelection=3)
    collectDataForSort(sorter, 'ClassicQuicksort', file, dataLength)


def collectDataForDualPivotQuicksort(data, file, dataLength):

    ################# FIRST, LAST PIVOT SELECTION ######################
    sorter = DualPivotQuicksort(list(data))
    collectDataForSort(sorter, 'DualPivotQuicksort', file, dataLength)

    sorter = DualPivotQuicksort(list(data), doInsertionSort=True, insertionSortThreshold=17)
    collectDataForSort(sorter, 'DualPivotQuicksort', file, dataLength)

    sorter = DualPivotQuicksort(list(data), behaveOptimally=True)
    collectDataForSort(sorter, 'OptimalDualPivotQuicksort', file, dataLength)

    sorter = DualPivotQuicksort(list(data),doInsertionSort=True, insertionSortThreshold=17, behaveOptimally=True)
    collectDataForSort(sorter, 'OptimalDualPivotQuicksort', file, dataLength)

    ################# TERTILES PIVOT SELECTION ######################
    sorter = DualPivotQuicksort(list(data), pivotSelection=2)
    collectDataForSort(sorter, 'DualPivotQuicksort', file, dataLength)

    sorter = DualPivotQuicksort(list(data), doInsertionSort=True, insertionSortThreshold=17, pivotSelection=2)
    collectDataForSort(sorter, 'DualPivotQuicksort', file, dataLength)

    sorter = DualPivotQuicksort(list(data), behaveOptimally=True, pivotSelection=2)
    collectDataForSort(sorter, 'OptimalDualPivotQuicksort', file, dataLength)

    sorter = DualPivotQuicksort(list(data),doInsertionSort=True, insertionSortThreshold=17, behaveOptimally=True, pivotSelection=2)
    collectDataForSort(sorter, 'OptimalDualPivotQuicksort', file, dataLength)

def sortData(data):
    fileName = 'data' + str(len(data)) + '.csv'

    file = open(fileName, 'w')

    # write the header
    file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ("Name", "Length", "Median Selection", "Num Pivots", "Used Insertion Sort", "Insertion Sort Threshold", "Time", "Comparisons", "Swaps"))

    dataLength = len(data)
    print dataLength

    collectDataForClassicQuicksort(data, file, dataLength)
    collectDataForDualPivotQuicksort(data, file, dataLength)


    sorter = YaroslavskiyQuicksort(list(data))
    collectDataForSort(sorter, 'YaroslavskiyQuicksort', file, dataLength)

    sorter = ThreePivotQuicksort(list(data))
    collectDataForSort(sorter, 'ThreePivotQuicksort', file, dataLength)

    for i in range(3,7):
        sorter = MPivotQuicksort(list(data), i)
        collectDataForSort(sorter, 'MPivotQuicksort', file, dataLength)

        sorter = MPivotQuicksort(list(data), i, minHeapOptimization=True)
        collectDataForSort(sorter, 'HeapOptimizedMPivotQuicksort', file, dataLength)

    file.close()

def run(minLength, maxLength, lowerRange, upperRange):

    pool = ThreadPool(4)

    # data = []
    # for a in generateData(minLength, maxLength, lowerRange, upperRange):
    #     # print a
    #     data.append(a)

    results = pool.map(sortData, generateData(minLength, maxLength, lowerRange, upperRange))

    pool.close()
    pool.join()

    print results

def processDataFiles():

    dataFiles = [a for a in os.listdir(os.curdir) if re.match("data\d+\.csv", a)]

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