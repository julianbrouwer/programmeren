import csv
max = -9
with open('csv bestand', 'r') as scoreFile:
    scoreFileReader = csv.reader(scoreFile,  delimiter=';')
    for row in scoreFileReader:
        if int(row[2]) > max:
            max = int(row[2])
print(max)

scoreFile.close()
