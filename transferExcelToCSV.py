from doctest import OutputChecker
import pandas as pd
import os

def transferExcelToCSV(targetPath, outputPath):

    # Read 1st sheet of excel file
    data = pd.read_excel(targetPath, index_col=None)

    # Output csv format
    data.to_csv(outputPath, encoding='utf-8', index=0)


def transferAllFiles(directoryPath):
    for currentDir, subDir, filesList in os.walk(directoryPath):
        for fileName in filesList:
            targetPath = os.path.join(currentDir, fileName)
            fileName = os.path.splitext(os.path.basename(targetPath))[0] + '.csv'
            outputPath = os.path.join(currentDir, fileName)

            print(outputPath)
            
            #Call function
            transferExcelToCSV(targetPath, outputPath)

transferAllFiles('C:/Users/xxx/Downloads/test')