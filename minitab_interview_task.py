import csv

csvContent = []

def confirmPath(path):
    valueList = []
    
    try:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                valueList = []
                for value in row:
                    valueList.append(value)
                csvContent.append(valueList)
    except:
        return False

    return True

def askForSortInfo(sortInfo):
    validInfo = False
    sortTypes = ["alpha", "numeric", "both"]
    sortOrders = ["ascending", "descending"]

    while (validInfo == False):
        localSortInfo = input("Enter the " + sortInfo + ": ")

        if (sortInfo == "sort type"):
            if (localSortInfo in sortTypes):
                validInfo = True
            else:
                print("That is not a valid " + sortInfo + ".")
        else:
            if (localSortInfo in sortOrders):
                validInfo = True
            else:
                print("That is not a valid " + sortInfo + ".")

    return localSortInfo
    

def askForPath():
    inputtedPath = ""
    pathConfirmed = False
    
    while (pathConfirmed == False):
        inputtedPath = input("Enter the path to the CSV file: ")

        if (confirmPath(inputtedPath) == True):
            pathConfirmed = True
        else:
            print('That file does not exist.')

def sortAlpha():
    sortedData = []
    
    for row in csvContent:
        sortedInner = []
        for value in row:
            try:
                data = float(value)
            except:
                sortedInner.append(value)
        if (sortOrder == "ascending"):
            sortedInner.sort()
        else:
            sortedInner.sort(reverse = True)

        sortedData.append(sortedInner)

    return sortedData

def sortNumeric():
    sortedData = []

    for row in csvContent:
        rowData = []
        sortedInner = []
        for value in row:
            try:
                data = (value, float(value))
                rowData.append(data)
            except:
                pass

        if (sortOrder == "ascending"):
            rowData.sort(key = lambda x: x[1])
        else:
            rowData.sort(key = lambda x: x[1], reverse = True)

        for entry in rowData:
            sortedInner.append(entry[0])
            
        sortedData.append(sortedInner)

    return sortedData

def sortBoth():
    sortedData = []

    for row in csvContent:
        numericData = []
        sortedNumbers = []
        sortedStrings = []
        sortedInner = []
        for value in row:
            try:
                data = (value, float(value))
                numericData.append(data)
            except:
                sortedStrings.append(value)

        if (sortOrder == "ascending"):
            sortedStrings.sort()
            numericData.sort(key = lambda x: x[1])
            for entry in numericData:
                sortedNumbers.append(entry[0])
            sortedInner = sortedNumbers + sortedStrings
        else:
            sortedStrings.sort(reverse = True)
            numericData.sort(key = lambda x: x[1], reverse = True)
            for entry in numericData:
                sortedNumbers.append(entry[0])
            sortedInner = sortedStrings + sortedNumbers
        
        sortedData.append(sortedInner)

    return sortedData

def printContents(outputContent):
    for array in outputContent:
        for element in range(len(array)):
            if (element != len(array) - 1):
                print(array[element], end = ", ")
            else:
                print(array[element])
    
def sortLines():
    outputContent = []

    if (sortType == "alpha"):
        outputContent = sortAlpha()

    elif (sortType == "numeric"):
        outputContent = sortNumeric()

    else:
        outputContent = sortBoth()
            
    printContents(outputContent)
    
askForPath()
sortType = askForSortInfo("sort type")
sortOrder = askForSortInfo("sort order")
sortLines()    
