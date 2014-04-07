from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

fileName = 'alldata.csv'

dataAbsPath = '../quicksorts/' + fileName

DEBUG = False

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


        sizeList = np.array(sizeList, dtype = np.int64)
        timeList = np.array(timeList, dtype = np.float64)
        compList = np.array(compList, dtype = np.int64)
        swapList = np.array(swapList, dtype = np.int64)

        data[label] = sizeList,timeList,compList,swapList

    return averageData(data)

def averageData(data):
    '''
    This function will take in the data dictionary and average all the data
    points with the same size value
    '''

    for label in data.keys() :
        sizeList,timeList,compList,swapList = data[label]


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


        sizeList = np.array(sizeListTemp,dtype = np.int64)
        timeList = np.array(timeListTemp,dtype = np.float128)
        compList = np.array(compListTemp,dtype = np.int64)
        swapList = np.array(swapListTemp,dtype = np.int64)

        data[label] = sizeList,timeList,compList,swapList

    return data

def markerGenerator(index,withSymbol= True, withColor = True):
    '''
    This function was created so that we can generate lines
    with varying symbols and colors without creating them by
    hand.
    '''

    colors = 'rbgmcky'
    numColors = len(colors)
    markers = 'ox^spdv><'
    numMarkers = len(markers)

    return withSymbol*markers[index%numMarkers]+withColor*colors[index%numColors]

def convertLabelToStr(label):
    name,medianSelection,numPivots,usedInsertionSort = label
    return "%s - %s - %s" %(name,medianSelection,numPivots)

def plotData(data,  plotTime = False, 
                    plotComp = True, 
                    plotSwap = True,
                    goodFunction = lambda x:True , 
                    badFunction = lambda x:False, 
                    makeLegend = True,
                    legendSize = 10, 
                    plotTitle = None,
                    fontsize = 12,
                    plotter = plt.plot,
                    connectDataPoints = False,
                    xlim = None,
                    specialFlag = False) :
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
    :param legendSize: size of the legend
    :param plotTitle: string of title of the plot. Will be placed on the top of the figure.
    :param fontsize: The font size of the title of the figure
    :param plotter: function that will plot the data ( plt.plot, plt.semilogx, plt.semilogy, plt.loglog )
    :param connectDataPoints: boolean to control if the data points will be connected with a solid line
    '''

    keyList = list(data.keys())
    keyList.sort()

    #print keyList

    if plotTime :
        timeFigure = plt.figure()
    if plotComp :
        compFigure = plt.figure()
    if plotSwap :
        swapFigure = plt.figure()

    if xlim and xlim[0] > xlim[1]:

        xlim[1],xlim[0] = xlim[0],xlim[1]

    for count,label in enumerate(keyList):

        marker = connectDataPoints*'-' + markerGenerator(count)

        if goodFunction(label) and not badFunction(label) :
            sizeList,timeList,compList,swapList = data[label]

            if specialFlag :
                timeList = timeList/( sizeList*np.log2(sizeList) )
                compList = compList/( sizeList*np.log2(sizeList) )
                swapList = swapList/( sizeList*np.log2(sizeList) )
                sizeList = np.log2(sizeList)

            if plotTime :
                plt.figure(timeFigure.number)
                plotter(sizeList,timeList,marker,label=convertLabelToStr(label))
            if plotComp :
                plt.figure(compFigure.number)
                plotter(sizeList,compList,marker,label=convertLabelToStr(label))
            if plotSwap :
                plt.figure(swapFigure.number)
                plotter(sizeList,swapList,marker,label=convertLabelToStr(label))

            if DEBUG:
                index = ( xlim[0] <= sizeList) * (sizeList <= xlim[1] )
                print ""
                print convertLabelToStr(label)
                print sizeList[index]
                print compList[index]
                print swapList[index]

    returnList = []

    legendProp = {'size':legendSize}

    if xlim:
        timeYLim,compYLim,swapYLim = extractYLim(data, goodFunction, badFunction, xlim)

    if plotTime :
        returnList.append(timeFigure)
        plt.figure(timeFigure.number)
        plt.xlabel('Size')
        plt.ylabel('Time')
        
        if makeLegend :
            plt.legend(loc = "upper left",prop = legendProp)

        if plotTitle:
            plt.title(plotTitle + ' (Time)',fontsize = fontsize)

        if xlim:
            plt.xlim(xlim[0],xlim[1])
            plt.ylim(timeYLim[0],timeYLim[1])

    if plotComp :
        returnList.append(compFigure)
        plt.figure(compFigure.number)
        plt.xlabel('Size')
        plt.ylabel('Comparisons')

        if makeLegend :
            plt.legend(loc = "upper left",prop = legendProp)

        if plotTitle:
            plt.title(plotTitle + ' (Comparisons)',fontsize = fontsize)

        if xlim:
            plt.xlim(xlim[0],xlim[1])
            plt.ylim(compYLim[0],compYLim[1])

    if plotSwap:
        returnList.append(swapFigure)
        plt.figure(swapFigure.number)
        plt.xlabel('Size')
        plt.ylabel('Swaps')

        if makeLegend :
            plt.legend(loc = "upper left",prop = legendProp)

        if plotTitle:
            plt.title(plotTitle + ' (Swaps)',fontsize = fontsize)

        if xlim:
            plt.xlim(xlim[0],xlim[1])
            plt.ylim(swapYLim[0],swapYLim[1])

    if specialFlag and plotTime:
        plt.figure(timeFigure.number)
        plt.xlabel('log(Size)')
        plt.ylabel('Time / (Size log(Size) )')

    if specialFlag and plotComp:
        plt.figure(compFigure.number)
        plt.xlabel('log(Size)')
        plt.ylabel('Comparisons / (Size log(Size) )')

    if specialFlag and plotSwap:
        plt.figure(swapFigure.number)
        plt.xlabel('log(Size)')
        plt.ylabel('Swaps / (Size log(Size) )')

    return tuple(returnList)

def plotPolynomialFit(data,fitParameters,figureList,
                    plotComp = True, 
                    plotSwap = True,
                    goodFunction = lambda x:True , 
                    badFunction = lambda x:False, 
                    makeLegend = True, 
                    legendSize = 10, 
                    plotter = plt.plot,
                    xlim = None,
                    linewidth = 1.5,
                    numPoints = 10**3,
                    specialFlag = False) :

    keyList = list(data.keys())
    keyList.sort()

    #print keyList
    count = 0
    if plotComp :
        compFigure = figureList[count]
        count+=1
    if plotSwap :
        swapFigure = figureList[count]
        count+=1

    if xlim and xlim[0] > xlim[1]:

        xlim[1],xlim[0] = xlim[0],xlim[1]

    for count,label in enumerate(keyList):

        if count < 7 :
            marker = '--' + markerGenerator(count,withSymbol=False)
        else:
            marker = '-' + markerGenerator(count,withSymbol=False)

        if goodFunction(label) and not badFunction(label) :
            sizeList,timeList,compList,swapList = data[label]
            compCoef,swapCoef = fitParameters[label]

            if xlim :
                xMin = min( min(sizeList),xlim[0])
                xMax = max( max(sizeList),xlim[1])
            else :
                xMin = min(sizeList)
                xMax = max(sizeList)

            xVals = np.linspace(xMin,xMax,numPoints)

            if plotComp :
                compFitFunc = lambda xx:fitFunction(xx,*tuple(compCoef))

                if specialFlag :
                    # Plot something special
                    yVals = compFitFunc(xVals) / ( xVals * np.log2(xVals) )
                    xVals = np.log2(xVals)
                else:
                    yVals = compFitFunc(xVals)

                plt.figure(compFigure.number)
                plotter(xVals,yVals,marker,label=convertLabelToStr(label)+" Fit",linewidth = linewidth)

            if plotSwap :
                swapFitFunc = lambda xx:fitFunction(xx,*tuple(swapCoef))

                if specialFlag :
                    # Plot something special
                    yVals = swapFitFunc(xVals) / ( xVals * np.log2(xVals) )
                    xVals = np.log2(xVals)
                    print yVals
                else:
                    yVals = swapFitFunc(xVals)

                plt.figure(swapFigure.number)
                plotter(xVals,yVals,marker,label=convertLabelToStr(label)+" Fit",linewidth = linewidth)

    legendProp = {'size':legendSize}

    if xlim:
        timeYLim,compYLim,swapYLim = extractYLim(data, goodFunction, badFunction, xlim)

    if plotComp and makeLegend:
        plt.figure(compFigure.number)
        plt.legend(loc = "upper left",prop = legendProp)

    if plotSwap and xlim:
        plt.xlim(xlim[0],xlim[1])
        plt.ylim(compYLim[0],compYLim[1])

    if plotSwap and makeLegend:
        plt.figure(swapFigure.number)
        plt.legend(loc = "upper left",prop = legendProp)

    if plotSwap and xlim:
        plt.xlim(xlim[0],xlim[1])
        plt.ylim(swapYLim[0],swapYLim[1])

def extractYLim(data,goodFunction,badFunction,xlim):
    keyList = list(data.keys())
    keyList.sort()

    if xlim[0] > xlim[1]:

        xlim[1],xlim[0] = xlim[0],xlim[1]

    yMinTime = None
    yMaxTime = -1

    yMinComp = None
    yMaxComp = -1

    yMinSwap = None
    yMaxSwap = -1

    for label in keyList:
        if goodFunction(label) and not badFunction(label) :
            sizeList,timeList,compList,swapList = data[label]

            sizeIndex = (xlim[0] <= sizeList) * ( sizeList <= xlim[1]  )

            yMinTimeTemp = np.min(timeList[sizeIndex])
            yMaxTimeTemp = np.max(timeList[sizeIndex])

            yMinCompTemp = np.min(compList[sizeIndex])
            yMaxCompTemp = np.max(compList[sizeIndex])
            
            yMinSwapTemp = np.min(swapList[sizeIndex])
            yMaxSwapTemp = np.max(swapList[sizeIndex])

            if not bool(yMinTime) or yMinTime > yMinTimeTemp:
                yMinTime = yMinTimeTemp

            if yMaxTime < yMaxTimeTemp:
                yMaxTime = yMaxTimeTemp

            if not bool(yMinComp) or yMinComp > yMinCompTemp:
                yMinComp = yMinCompTemp

            if yMaxComp < yMaxCompTemp:
                yMaxComp = yMaxCompTemp

            if not bool(yMinSwap) or yMinSwap > yMinSwapTemp:
                yMinSwap = yMinSwapTemp

            if yMaxSwap < yMaxSwapTemp:
                yMaxSwap = yMaxSwapTemp


    if not bool(yMinTime):
        yMinTime = 0

    if not bool(yMinComp):
        yMinComp = 0

    if not bool(yMinSwap):
        yMinSwap = 0

    return [yMinTime,yMaxTime],[yMinComp,yMaxComp],[yMinSwap,yMaxSwap]


def calcLeastSquaresOnData(data):
    '''
    We want to fit the data to :
        y = A x log(x) + B x + C log(x)

    We use a non-linear curve fitter.

    Other considerations:

    Method 2 :
        y = A x log(x) + B

        So we make a transformation so that :
            X = x log(x) = x ln(x)/ln(2)
            Y = y

    Method 3:
        y = A x log(x) + Bx = x ( A log(x) + B )

        So we make a transformation so that :
            X = log(x) = ln(x)/ln(2)
            Y = y/x

    Method 3:
        y = A x log(x) + Blog(x) = log(x) ( A x + B )

        So we make a transformation so that :
            X = x
            Y = y/log(x)
    '''
    keyList = list(data.keys())
    keyList.sort()

    fitParameters = {}

    for label in keyList :
        sizeList,timeList,compList,swapList = data[label]

        sizeList = np.array(sizeList, dtype = np.float64)
        timeList = np.array(timeList, dtype = np.float64)
        compList = np.array(compList, dtype = np.float64)
        swapList = np.array(swapList, dtype = np.float64)

        compCoef,compCov = curve_fit(fitFunction, sizeList, compList)
        swapCoef,swapCov = curve_fit(fitFunction, sizeList, swapList)

        fitParameters[label] = compCoef,swapCoef

    print ""
    print "COMPARISON COEFFICIENTS"
    for label in keyList :
        compCoef,swapCoef = fitParameters[label]
        print "%40s | %9.5f | %9.4f | %9.4f "%(convertLabelToStr(label),compCoef[0],compCoef[1],compCoef[2])

    print ""
    print "SWAP COEFFICIENTS"
    for label in keyList :
        compCoef,swapCoef = fitParameters[label]
        print "%40s | %9.5f | %9.4f | %9.4f "%(convertLabelToStr(label),swapCoef[0],swapCoef[1],compCoef[2])

    return fitParameters

def fitFunction(xx,AA,BB,CC):
    return AA*xx*np.log2(xx)+BB*xx+CC*np.log2(xx)

def saveFigure(figure,fileName,fileExtention = '.png',dpi = 600):
    fullFileName = fileName + fileExtention
    plt.figure(figure.number)
    plt.savefig(fullFileName, 
                    dpi         = dpi, 
                    facecolor   = 'w', 
                    edgecolor   = 'w',
                    orientation = 'portrait', 
                    papertype   = None, 
                    format      = None,
                    transparent = True, 
                    bbox_inches = None, 
                    pad_inches  = 0.15,
                    frameon     = None)

def plotDataAndFit(data,fitParameters,
                    plotComp = True, 
                    plotSwap = True,
                    goodFunction = lambda x:True , 
                    badFunction = lambda x:False, 
                    makeLegend = True,
                    legendSize = 10, 
                    plotTitle = None,
                    fontsize = 12, 
                    plotter = plt.plot,
                    xlim = None,
                    connectDataPoints = False,
                    linewidth = 1.5,
                    numPoints = 10**3,
                    savePlot = False,
                    dpi = 600,
                    specialFlag = False) :

    figureList = plotData(data,
                    plotComp = plotComp, 
                    plotSwap = plotSwap,
                    goodFunction = goodFunction , 
                    badFunction = badFunction, 
                    makeLegend = makeLegend,
                    legendSize = legendSize, 
                    plotTitle = plotTitle,
                    xlim = xlim,
                    fontsize = fontsize,
                    plotter = plotter,
                    connectDataPoints = connectDataPoints,
                    specialFlag = specialFlag)

    if not connectDataPoints :
        plotPolynomialFit(data,fitParameters,figureList,
                        plotComp = plotComp, 
                        plotSwap = plotSwap,
                        goodFunction = goodFunction , 
                        badFunction = badFunction, 
                        makeLegend = makeLegend, 
                        legendSize = legendSize,
                        plotter = plotter,
                        xlim = xlim,
                        linewidth = linewidth,
                        numPoints = numPoints,
                        specialFlag = specialFlag)

    if savePlot :
        fileName = "".join(plotTitle.split() )
        compFigure,swapFigure = figureList
        saveFigure(compFigure,fileName+"_comp",fileExtention = '.png',dpi = dpi)
        saveFigure(swapFigure,fileName+"_swap",fileExtention = '.png',dpi = dpi)

    return figureList

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


    mPivotQuicksortOnly3 = lambda x : mPivotQuicksortOnly(x) and threePivot(x)

    customPlot = lambda x: classicQuickSortOnly(x) or dualPivotQuicksortOnly(x) or threePivotQuicksortOnly(x) or mPivotQuicksortOnly3(x)

    allMPivotQuicksortKinds = lambda x: mPivotQuicksortOnly(x) or heapOptimizedMPivotQuicksortOnly(x)

    data = getData(dataAbsPath)

    fitParameters = calcLeastSquaresOnData(data)

    maskFunctionList = [ classicQuickSortOnly,dualPivotQuicksortOnly,heapOptimizedMPivotQuicksortOnly,
                        mPivotQuicksortOnly, optimalDualPivotQuicksortOnly,threePivotQuicksortOnly,
                        yaroslavskiyQuicksortOnly, onePivot,twoPivot,threePivot,allMPivotQuicksortKinds]

    maskFunctionTitleList = ['Classic QuickSorts','Dual Pivot Quicksorts','Heap Optimized M-Pivot Quicksorts',
                            'Non Optimized M-Pivot Quicksorts','Optimal Dual Pivot Quicksorts','Three Pivot Quicksorts',
                            'Yaroslavskiy Quicksorts','One Pivots','Two Pivots','Three Pivots','M-Pivot Quicksorts']

    smallScaleLimits = [100,1000]

    plotDataAndFit(data,fitParameters, plotTitle = 'Legend Plot', connectDataPoints = True,legendSize=15,savePlot=True)
    plotDataAndFit(data,fitParameters, plotTitle = 'All the Plots Small Scale',xlim = smallScaleLimits, connectDataPoints = True,makeLegend=False,savePlot=True)
    plotDataAndFit(data,fitParameters, plotTitle = 'All the Plots Large Scale', connectDataPoints = True,makeLegend=False,savePlot = True)
    plotDataAndFit(data,fitParameters, plotTitle = 'Semilogx All Plots Large Scale ', connectDataPoints = True,makeLegend=False,savePlot = True,plotter = plt.semilogx)
    
    for maskFunc,plotTitle in zip(maskFunctionList,maskFunctionTitleList):
        plotDataAndFit(data, fitParameters,goodFunction = maskFunc, plotTitle = plotTitle+" Large Scale",savePlot = True)
    
    for maskFunc,plotTitle in zip(maskFunctionList,maskFunctionTitleList):
        plotDataAndFit(data, fitParameters,goodFunction = maskFunc, plotTitle = plotTitle+" Small Scale", xlim =smallScaleLimits,connectDataPoints = True,savePlot = True)    
    
    plotDataAndFit(data,fitParameters, goodFunction = allMPivotQuicksortKinds, plotTitle = "M-Pivot Quicksorts Large Scale",savePlot = True,legendSize=7)
    plotDataAndFit(data,fitParameters, goodFunction = allMPivotQuicksortKinds, plotTitle = "M-Pivot Quicksorts Small Scale",xlim = smallScaleLimits,connectDataPoints = True,savePlot = True,legendSize=7)


    # The special plot
    plotDataAndFit(data,fitParameters, plotTitle = 'All Plots Large Scale logn vs y_OVER_nlogn', connectDataPoints = True,makeLegend=False,savePlot = True,specialFlag = True)

    #plotDataAndFit(data,fitParameters, goodFunction = customPlot, plotTitle = plotTitle+" Large Scale",savePlot = True)
    #plotDataAndFit(data,fitParameters, goodFunction = customPlot, plotTitle = 'customPlot',xlim = smallScaleLimits,connectDataPoints = True,savePlot = True)

    #plt.show()

if __name__ == '__main__':
    main()