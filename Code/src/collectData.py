__author__ = 'paymahn'

import random
from time import time
import os
import argparse

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
    for i in mrange(minLength, maxLength, 9./5.):
        data = [random.randint(lowerBound, upperBound) for _ in range(i)]
        yield data

    return

def timeSort(sorter):
    start = time()
    sorter.sort()
    return time() - start

def getUnusedFileName(fileName):
    originalFileName = fileName
    i = 1
    while fileName in os.listdir(os.curdir):
        fileName = originalFileName[:-4] + str(i) + originalFileName[-4:]
        i+= 1

    return fileName

def run(fileName, lowerBound=2, upperBound=1e6, lowerRange=0, upperRange=1e8):


    file = open(fileName, 'w')

    # write the header
    file.write("%s,%s,%s,%s,%s,%s,%s\n" % ("Name", "Length", "Used Insertion Sort", "Insertion Sort Threshold", "Time", "Comparisons", "Swaps"))


    str = "%s,%d,%s,%d,%f,%d,%d\n"
    for data in generateData(lowerBound,upperBound, lowerRange, upperRange):

        dataLength = len(data)
        print dataLength

        sorter = ClassicQuicksort(list(data))
        sortTime = timeSort(sorter)
        file.write(str % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
        file.flush()

        sorter = ClassicQuicksort(list(data), True)
        sortTime = timeSort(sorter)
        file.write(str % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
        file.flush()

        sorter = ClassicQuicksort(list(data), True, 17)
        sortTime = timeSort(sorter)
        file.write(str % ('ClassicQuicksort', dataLength, sorter.doInsertionSort, sorter.insertionSortThreshold, sortTime, sorter.numComparisons, sorter.numSwaps))
        file.flush()

        sorter = YaroslavskiyQuicksort(list(data))
        sortTime = timeSort(sorter)
        file.write(str % ('YaroslavskiyQuicksort', dataLength, True, YaroslavskiyQuicksort.INSERTION_SORT_THRESHOLD, sortTime, sorter.numComparisons, sorter.numSwaps))
        file.flush()

        sorter = DualPivotQuicksort(list(data))
        sortTime = timeSort(sorter)
        file.write(str % ('DualPivot', dataLength, False, -1, sortTime, sorter.numComparisons, sorter.numSwaps))
        file.flush()

        sorter = DualPivotQuicksort(list(data), behaveOptimally=True)
        sortTime = timeSort(sorter)
        file.write(str % ('OptimalDualPivot', dataLength, False, -1, sortTime, sorter.numComparisons, sorter.numSwaps))
        file.flush()


    file.close()


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", help="The name of the file to write values to")
    parser.add_argument("-lb", "--lowerBound", type=int, default=2, help="The smallest list length that should be sorted. Default 2.")
    parser.add_argument("-ub", "--upperBound", type=int, default=1e8, help="The largest list length that should be sorted. Default 1e8.")
    parser.add_argument("-lr", "--lowerRange", type=int, default=0, help="The smallest value in the list. Default 0.")
    parser.add_argument("-ur", "--upperRange", type=int, default=1e9, help="The largest value in the list. Default 1e9.")
    parser.add_argument("-n", "--noNewFile", action="store_true", help="Don't create new file if the specified file already exists.")

    return parser.parse_args()

if __name__ == '__main__':
    # run('data.csv')
    args = getArgs()

    if not args.noNewFile:
        fileName = getUnusedFileName(args.fileName)
    else:
        fileName = args.fileName

    run(fileName, args.lowerBound, args.upperBound, args.lowerRange, args.upperRange)