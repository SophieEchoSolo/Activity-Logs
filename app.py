import csv
import datetime

actDict = dict()

def activityParse():
    with open("apriltomayactivity.csv", newline='') as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:
            for key, value in row.items():
                if key in actDict:
                    if not isinstance(actDict[key],list):
                        actDict[key]=[actDict[key]]
                    actDict[key].append(value)
                else:
                    actDict[key] = value
        
        return actDict

def getAvgs(actDict):
    avgDict = {}
    dateList=[]

    for key in actDict.keys():
        total = 0
        if key.lower() != "date":
            avgDict.update({key:[]})
            for val in actDict[key]:
                total+=float(val.replace(',',''))
            avgDict[key].append(round(total/len(actDict[key]),2))
        else:
            for val in actDict["Date"]:
                dates = datetime.datetime.strptime(val,"%Y-%m-%d")
                dateList.append(dates)

    print(f"The average values of each field for the time period of {str(dateList[0])} to {str(dateList[-1])} are as follows: {str(avgDict)}" )
            



if __name__ == "__main__":
    newDict = activityParse()
    getAvgs(newDict)
