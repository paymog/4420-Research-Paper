from matplotlib import pyplot as plt
import numpy as np

fileName = 'data.csv'

dataAbsPath = '../quicksorts/' + fileName

def getData(filePath):

    flink = open(filePath,'r')

    data = {}

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

        data[label] = sizeList,timeList,compList,swapList

    return averageData(data)

def averageData(data):
    '''
    This function will take in the data dictionary and average all the data
    points with the same size value
    '''

    for label in data.keys() :
        sizeList,timeList,compList,swapList = data[label]

        sizeList = np.array(sizeList)
        timeList = np.array(timeList)
        compList = np.array(compList)
        swapList = np.array(swapList)


        sizeListTemp = []
        timeListTemp = []
        compListTemp = []
        swapListTemp = []

        for size in np.nditer(sizeList):

            if size not in sizeListTemp:
                sizeListTemp.append(size)

                indexArray = size == sizeList
                numValues = len(indexArray) * 1.0

                # The averages
                timeTemp = np.sum(timeList[ indexArray ])/numValues
                compTemp = np.sum(compList[ indexArray ])/numValues
                swapTemp = np.sum(swapList[ indexArray ])/numValues

                timeListTemp.append(timeTemp)
                compListTemp.append(compTemp)
                swapListTemp.append(swapTemp)


        sizeList = np.array(sizeListTemp)
        timeList = np.array(timeListTemp)
        compList = np.array(compListTemp)
        swapList = np.array(swapListTemp)

        data[label] = sizeList,timeList,compList,swapList

    return data

def plotData(data, plotTime = False, plotComp = True, plotSwap = True,goodFunction = lambda x:True , badFunction = lambda x:False, makeLegend = True) :
    '''
    Plot data will take the data dictionary and create plots according to the key word argunments.

    Note that labels are defined as follows (name,medianSelection,numPivots,usedInsertionSort)

    :param data: the dictionary that contains data to be plotted
    :param plotTime: boolean to control if the size vs time plots will actually be rendered
    :param plotComp: boolean to control if the size vs comparisons plots will actually be rendered
    :param plotSwap: boolean to control if the size vs swaps plots will actually be rendered
    :param goodFunction: a function that will take in the label tuple and determine if it will plot that label
    :param badFunction:  a function that will take in the label tuple and determine if it will not plot that label
    :param makeLegend: boolean to control if the legend should be rendered
    '''

    marker = '-x'

    keyList = list(data.keys())
    keyList.sort()

    #print keyList

    if plotTime :
        timeFigure = plt.figure()
    if plotComp :
        compFigure = plt.figure()
    if plotSwap :
        swapFigure = plt.figure()

    for label in keyList :

        if goodFunction(label) and not badFunction(label) :
            sizeList,timeList,compList,swapList = data[label]

            if plotTime :
                plt.figure(timeFigure.number)
                plt.plot(sizeList,timeList,marker,label=str(label))
            if plotComp :
                plt.figure(compFigure.number)
                plt.plot(sizeList,compList,marker,label=str(label))
            if plotSwap :
                plt.figure(swapFigure.number)
                plt.plot(sizeList,swapList,marker,label=str(label))

    returnList = []

    if plotTime :
        returnList.append(timeFigure)
        plt.figure(timeFigure.number)
        plt.xlabel('Size')
        plt.ylabel('Time')
        
        if makeLegend :
            plt.legend(loc = "upper left")

    if plotComp :
        returnList.append(compFigure)
        plt.figure(compFigure.number)
        plt.xlabel('Size')
        plt.ylabel('Comparisons')

        if makeLegend :
            plt.legend(loc = "upper left")

    if plotSwap:
        returnList.append(swapFigure)
        plt.figure(swapFigure.number)
        plt.xlabel('Size')
        plt.ylabel('Swaps')

        if makeLegend :
            plt.legend(loc = "upper left")

    plt.show()

    return tuple(returnList)

def main():
    # Note that labels are defined as follows 
    # (name,medianSelection,numPivots,usedInsertionSort)
    #
    # List of all labels as of April 4
    #
    # ('ClassicQuicksort', 1, 1, True)
    # ('ClassicQuicksort', 2, 1, True)
    # ('ClassicQuicksort', 3, 1, True)
    # ('DualPivotQuicksort', 1, 2, True)
    # ('DualPivotQuicksort', 2, 2, True)
    # ('HeapOptimizedMPivotQuicksort', 1, 3, True)
    # ('HeapOptimizedMPivotQuicksort', 1, 4, True)
    # ('HeapOptimizedMPivotQuicksort', 1, 5, True)
    # ('HeapOptimizedMPivotQuicksort', 1, 6, True)
    # ('MPivotQuicksort', 1, 3, True)
    # ('MPivotQuicksort', 1, 4, True)
    # ('MPivotQuicksort', 1, 5, True)
    # ('MPivotQuicksort', 1, 6, True)
    # ('OptimalDualPivotQuicksort', 1, 2, True)
    # ('OptimalDualPivotQuicksort', 2, 2, True)
    # ('ThreePivotQuicksort', 1, 3, True)
    # ('YaroslavskiyQuicksort', 1, 2, True)

    classicQuickSortOnly             = lambda x: x[0] == 'ClassicQuicksort'
    dualPivotQuicksortOnly           = lambda x: x[0] == 'DualPivotQuicksort'
    heapOptimizedMPivotQuicksortOnly = lambda x: x[0] == 'HeapOptimizedMPivotQuicksort'
    mPivotQuicksortOnly              = lambda x: x[0] == 'MPivotQuicksort'
    optimalDualPivotQuicksortOnly    = lambda x: x[0] == 'OptimalDualPivotQuicksort'
    threePivotQuicksortOnly          = lambda x: x[0] == 'ThreePivotQuicksort'
    yaroslavskiyQuicksortOnly        = lambda x: x[0] == 'YaroslavskiyQuicksort'

    onePivot = lambda x: x[2] == 1
    twoPivot = lambda x: x[2] == 2
    threePivot = lambda x: x[2] == 3

    usedInsertionSort = lambda x: x[3]

    data = getData(dataAbsPath)

    plotData(data,makeLegend=False)

    #plotData(data, goodFunction = classicQuickSortOnly)
    #plotData(data, goodFunction = dualPivotQuicksortOnly)
    #plotData(data, goodFunction = heapOptimizedMPivotQuicksortOnly)
    #plotData(data, goodFunction = mPivotQuicksortOnly)
    #plotData(data, goodFunction = optimalDualPivotQuicksortOnly)
    #plotData(data, goodFunction = threePivotQuicksortOnly)
    #plotData(data, goodFunction = yaroslavskiyQuicksortOnly)

    #plotData(data, goodFunction = onePivot)
    #plotData(data, goodFunction = twoPivot)
    #plotData(data, goodFunction = threePivot)

    #plotData(data, goodFunction = usedInsertionSort)


    mPivotQuicksortOnly3 = lambda x : mPivotQuicksortOnly(x) and threePivot(x)

    customPlot = lambda x: classicQuickSortOnly(x) or dualPivotQuicksortOnly(x) or threePivotQuicksortOnly(x) or mPivotQuicksortOnly3(x)

    plotData(data, goodFunction = customPlot)

if __name__ == '__main__':
    main()