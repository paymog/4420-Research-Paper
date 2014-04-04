__author__ = 'paymahn'

import os
import re

filesToIgnore = set(['data.csv'])

with open('temp.csv', 'w') as outfile:
    # write the header
    outfile.writelines("Name,Length,Median Selection,Num Pivots,Used Insertion Sort,Insertion Sort Threshold,Time,Comparisons,Swaps\n")
    for fileName in os.listdir(os.curdir):

        # determine whether the file should be processed
        if re.search("\.csv$", fileName) and fileName != outfile.name and fileName not in filesToIgnore:
            print fileName
            with open(fileName, 'r') as currFile:
                outfile.writelines(currFile.readlines()[1:])

            os.remove(fileName)


# after writing everything to the temp file, copy the data to a "real" file and  remove the temp file
import shutil
shutil.copy(outfile.name, 'alldata.csv')
os.remove(outfile.name)