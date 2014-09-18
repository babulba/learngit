import csv
fObj=open("player_regular_season.csv","rU")
csvReader=csv.reader(fObj)

for row in csvReader:
    print row

fObj.close()