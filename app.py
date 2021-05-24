import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

actDict = dict()

def activityParse():
    with open("input.csv", newline='') as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:
            for key, value in row.items():
                if key in actDict:
                    if not isinstance(actDict[key],list):
                        actDict[key]=[actDict[key]]
                    actDict[key].append(value)
                else:
                    actDict[key] = value
        for key in actDict.keys():
            if key.lower() != "date" and key.lower() != "floors":
                actDict.update({key:0})
                for val in actDict[key]:
                    val=float(val.replace(',',''))
                actDict.update({key: val})
            else:
                for val in actDict["Date"]:
                    val = datetime.datetime.strptime(val,"%Y-%m-%d")
                    actDict["Date"] = val
        
        return actDict

def getAvgs(actDict):
    avgDict = {}
    dateList=[]

    for key in actDict.keys():
        total = 0
        if key.lower() != "date" and key.lower() != "floors":
            avgDict.update({key:0})
            for val in actDict[key]:
                total+=float(val.replace(',',''))
            avgDict.update({key: round(total/len(actDict[key]),2)})
        else:
            for val in actDict["Date"]:
                dates = datetime.datetime.strptime(val,"%Y-%m-%d")
                dateList.append(dates)

    print(f"The average values of each field for the time period of {str(dateList[0])} to {str(dateList[-1])} are as follows: {str(avgDict)}" )
    return avgDict
            
def writeExcel(avgDict):
    with open('output.csv', 'w', newline='') as csvfile:
        fileWriter = csv.writer(csvfile)
        for key, value in avgDict.items():
            fileWriter.writerow([key, value])

#test plot
def plotData(actDict):

    for k, v in actDict.items():
        plt.title(k.upper())
        plt.xlabel("Days")
        plt.ylabel("y")
        plt.figure(k)
        xs = range(0,len(v))
        ys = v
        plt.plot(xs, ys, '-,', label=k)
        plt.legend()
        plt.savefig(f"{k.replace(' ', '-')}-plot.png")


if __name__ == "__main__":
    newDict = activityParse()
    newAvgs = getAvgs(newDict)
    writeExcel(newAvgs)
    plotData(newDict)