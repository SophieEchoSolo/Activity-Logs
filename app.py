import fitbit
import datetime
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import json
from functools import reduce
from fitauth import *


def activityParse(activities):
    # print(activities)
    # Needs to be updated due to fitauth implementation
    return activities


def getAvgs(actDict):
    # Needs to be updated due to fitauth implementation
    avgDict = {}
    dateList = []

    for key in actDict.keys():
        total = 0
        if key.lower() != "date" and key.lower() != "floors":
            avgDict.update({key: 0})
            for val in actDict[key]:
                print(val)
                total += val
            avgDict.update({key: round(total/len(actDict[key]), 2)})
        else:
            for val in actDict["Date"]:
                dateList.append(val)

    print(
        f"The average values of each field for the time period of {str(dateList[0])} to {str(dateList[-1])} are as follows: {str(avgDict)}")
    return avgDict


def plotData(actDict):

    for k, v in actDict.items():
        plt.title(k.upper())
        plt.xlabel("Days")
        plt.ylabel("y")
        plt.figure(k)
        xs = range(0, len(v))
        ys = v
        plt.plot(xs, ys, '-,', label=k)
        plt.legend()
        plt.savefig(f"{k.replace(' ', '-')}-plot.png")


if __name__ == "__main__":
    actList = ["activities/calories", "activities/steps"]
    load_dotenv()
    KEY = os.getenv('CONSUMER_KEY')
    SECRET = os.getenv('CONSUMER_SECRET')
    auth = loadAuth()
    authd_client = fitbit.Fitbit(KEY, SECRET,
                                 access_token=auth['access_token'], refresh_token=auth["refresh_token"], refresh_cb=saveAuth, expires_at=auth["expires_at"])
    newDict = activityParse(reduce(mergeDict, map(lambda a: authd_client.time_series(
        a, period="1d"), actList)))
    newAvgs = getAvgs(newDict)
    # plotData(newDict)
