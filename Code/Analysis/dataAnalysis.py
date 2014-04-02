from matplotlib import pyplot as plt
import numpy as np

fileName = 'data.csv'

dataAbsPath = '../quicksorts/' + fileName

def getData(filePath):

    flink = open(filePath,'r')

    data = {}

    # OptimalDualPivotQuicksort,1007,1,2,False,10,0.712151,10927,4759
    header = "Name,Length,Median Selection,Num Pivots,Used Insertion Sort,Insertion Sort Threshold,Time,Comparisons,Swaps\n"

    isFirst = True

    for line in flink:
        if line not in header and len(line) > 0 and line!=header:

            isNoError = True
            
            temp = line.strip().split(',')

            name = temp[0]
            
            try:
                length = int(temp[1])
            except:
                print "Error:",temp[1]
                isNoError = False            

            try:    
                medianSelection = int(temp[2])
            except:
                print "Error:",temp[2]
                isNoError = False

            try:    
                numPivots = int(temp[3])
            except:
                print "Error:",temp[3]
                isNoError = False

            try:    
                usedInsertionSort = bool(temp[4])
            except:
                print "Error:",temp[4]
                isNoError = False

            try:    
                insertionSortThreshold = int(temp[5]) # will not use
            except:
                print "Error:",temp[5]
                isNoError = False

            try:    
                time = float(temp[6])
            except:
                print "Error:",temp[6]
                isNoError = False

            try:    
                comparisons = int(temp[7])
            except:
                print "Error:",temp[7]
                isNoError = False

            try:    
                swaps = int(temp[8])
            except:
                print "Error:",temp[8]
                isNoError = False

            if isNoError:
                label = ( name,medianSelection,numPivots,usedInsertionSort)

                if label in data :
                    sizeList,timeList,compList,swapList = data[label]
                else:
                    sizeList = []
                    timeList = []
                    compList = []
                    swapList = []

                sizeList.append(length)
                timeList.append(time)
                compList.append(comparisons)
                swapList.append(swaps)

                data[label] = sizeList,timeList,compList,swapList

    for label in data.keys() :
        sizeList,timeList,compList,swapList = data[label]

        tempList = zip(sizeList,timeList,compList,swapList)

        tempList.sort()

        sizeList = [ item[0] for item in tempList]
        timeList = [ item[1] for item in tempList]
        compList = [ item[2] for item in tempList]
        swapList = [ item[3] for item in tempList]

    return data

def main():

    data = getData(dataAbsPath)

    timeFigureIndex = 1
    compFigureIndex = 2
    swapFigureIndex = 3

    marker = '-x'

    for label in data.keys() :

        sizeList,timeList,compList,swapList = data[label]

        plt.figure(timeFigureIndex)
        plt.plot(sizeList,timeList,marker,label=str(label))

        plt.figure(compFigureIndex)
        plt.plot(sizeList,compList,marker,label=str(label))

        plt.figure(swapFigureIndex)
        plt.plot(sizeList,swapList,marker,label=str(label))


    plt.figure(timeFigureIndex)
    plt.xlabel('Size')
    plt.ylabel('Time')

    plt.figure(compFigureIndex)
    plt.xlabel('Comparisons')
    plt.ylabel('Time')

    plt.figure(swapFigureIndex)
    plt.xlabel('Swaps')
    plt.ylabel('Time')

    plt.show()

if __name__ == '__main__':
    main()