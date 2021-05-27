import fitbit
import datetime
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import json
from functools import reduce
from fitauth import *
import pandas as pd

TEST_DATA = {'activities-calories': [{'dateTime': '2021-05-19', 'value': '2361'}, {'dateTime': '2021-05-20', 'value': '3188'}, {'dateTime': '2021-05-21', 'value': '2832'}, {'dateTime': '2021-05-22', 'value': '2767'}, {'dateTime': '2021-05-23', 'value': '2665'}, {'dateTime': '2021-05-24', 'value': '2847'}, {'dateTime': '2021-05-25', 'value': '1920'}],
             'activities-steps': [{'dateTime': '2021-05-19', 'value': '1148'}, {'dateTime': '2021-05-20', 'value': '7671'}, {'dateTime': '2021-05-21', 'value': '5667'}, {'dateTime': '2021-05-22', 'value': '4629'}, {'dateTime': '2021-05-23', 'value': '4555'}, {'dateTime': '2021-05-24', 'value': '5314'}, {'dateTime': '2021-05-25', 'value': '4237'}]}


def activityParse(activities):
    for key, val in activities.items():
        for index in range(len(val)):
            for key in val[index]:
                if key.lower() == "datetime":
                    newVal = datetime.datetime.strptime(
                        val[index][key], "%Y-%m-%d").date()
                    val[index].update({key: newVal})
                else:
                    newVal = float(val[index][key].replace(',', ''))
                    val[index].update({key: newVal})
    return activities


def getDataframes(actDict):
    # Need to sort out plots stacking
    for key in actDict.keys():
        df = pd.DataFrame()
        df = pd.DataFrame(data=newDict[key])
        df = df.sort_values('dateTime', ascending=True)

        plt.title(key.upper())
        plt.xlabel("Dates")
        plt.ylabel(key[key.find('-')+1:].capitalize())
        plt.plot(df['dateTime'], df['value'])
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(f"{key}-plot.png")


if __name__ == "__main__":
    actList = ["activities/calories", "activities/steps"]
    load_dotenv()
    KEY = os.getenv('CONSUMER_KEY')
    SECRET = os.getenv('CONSUMER_SECRET')
    auth = loadAuth()
    authd_client = fitbit.Fitbit(KEY, SECRET,
                                 access_token=auth['access_token'], refresh_token=auth["refresh_token"], refresh_cb=saveAuth, expires_at=auth["expires_at"])

    # activityData = reduce(mergeDict, map(lambda a: authd_client.time_series(
    #     a, period="7d"), actList))

    activityData = TEST_DATA
    newDict = activityParse(activityData)
    getDataframes(newDict)
