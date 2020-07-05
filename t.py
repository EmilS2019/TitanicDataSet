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
def getRowFromFile(csv_reader, rowNumber):
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[rowNumber])
            line_count += 1
            print(f'Processed {line_count} lines.')



theFile = getFile()
print(theFile)
#print(getRowFromFile(file, 1))

# with open('train.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             #print(f'\t{row[2]} works in the {row[1]} department, and was born {row[0]} years ago.')
#             print(row[8])
#             line_count += 1
#     print(f'Processed {line_count} lines.')