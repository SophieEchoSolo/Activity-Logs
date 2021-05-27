import fitbit
import datetime
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
from fitauth import *
import pandas as pd


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
    for key in actDict.keys():
        plt.clf()
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
    actList = ["activities/calories", "activities/steps", "activities/distance", "activities/minutesSedentary",
               'activities/minutesLightlyActive', 'activities/minutesFairlyActive', 'activities/minutesVeryActive', 'activities/activityCalories']
    load_dotenv()
    KEY = os.getenv('CONSUMER_KEY')
    SECRET = os.getenv('CONSUMER_SECRET')
    auth = loadAuth()
    authd_client = fitbit.Fitbit(KEY, SECRET,
                                 access_token=auth['access_token'], refresh_token=auth["refresh_token"], refresh_cb=saveAuth, expires_at=auth["expires_at"])

    activityData = reduce(mergeDict, map(
        lambda a: authd_client.time_series(a, period="30d"), actList))

    newDict = activityParse(activityData)
    getDataframes(newDict)
