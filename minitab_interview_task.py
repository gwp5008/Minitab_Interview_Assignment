import csv

def confirmPath(inputtedPath):
    global path
    path = inputtedPath

    try:
        with open(path) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=',')

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
            print("That file does not exist.")

def sortAlpha(valueList):
    sortedData = []

    for value in valueList:
        try:
            data = float(value)
        except:
            sortedData.append(value)
            
        if (sortOrder == "ascending"):
            sortedData.sort()
        else:
            sortedData.sort(reverse = True)

    return sortedData

def sortNumeric(valueList):
    sortedData = []
    sortedInner = []
    
    for value in valueList:
        try:
            data = (value, float(value))
            sortedInner.append(data)
        except:
            pass

    if (sortOrder == "ascending"):
        sortedInner.sort(key = lambda x: x[1])
    else:
        sortedInner.sort(key = lambda x: x[1], reverse = True)

    for entry in sortedInner:
        sortedData.append(entry[0])
            
    return sortedData

def sortBoth(valueList):
    sortedData = []

    sortedNumbers = sortNumeric(valueList)
    sortedStrings = sortAlpha(valueList)

    if (sortOrder == "ascending"):
        sortedData = sortedNumbers + sortedStrings

    else:
        sortedData = sortedStrings + sortedNumbers

    return sortedData

def printContents(outputContent):
    for element in range(len(outputContent)):
        if (element != len(outputContent) - 1):
            print(outputContent[element], end = ", ")
        else:
            print(outputContent[element])
    
def sortLines():
    outputContent = []

    with open(path) as csv_file:
        csvReader = csv.reader(csv_file, delimiter=',')

        for row in csvReader:
            valueList = []
                
            for value in row:
                valueList.append(value)

            if (sortType == "alpha"):
                outputContent = sortAlpha(valueList)

            elif (sortType == "numeric"):
                outputContent = sortNumeric(valueList)

            else:
                outputContent = sortBoth(valueList)

            printContents(outputContent)
    
askForPath()
sortType = askForSortInfo("sort type")
sortOrder = askForSortInfo("sort order")
sortLines()    
