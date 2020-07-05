import csv

def getFile():
    with open('train.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        output = {}
        i = 1
        for row in csv_reader:
            output[i] = row
            i+=1
        return output

#Column names are PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
def getRowFromFile(theFile, rowNumber):
    output = {}
    for i in range(2, len(theFile)):
        output[i] = theFile[i][rowNumber]
    return output

theFile = getFile()
getRowFromFile(theFile, 1)