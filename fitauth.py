import fitbit
from dotenv import load_dotenv
import os
import json
from functools import reduce

# activities/calories
# activities/steps
# activities/distance
# activities/minutesSedentary
# activities/minutesLightlyActive
# activities/minutesFairlyActive
# activities/minutesVeryActive
# activities/activityCalories
actList = ["activities/calories", "activities/steps", "activities/distance", "activities/minutesSedentary",
           'activities/minutesLightlyActive', 'activities/minutesFairlyActive', 'activities/minutesVeryActive', 'activities/activityCalories']


def mergeDict(dict1, dict2):
    dict1.update(dict2)
    return dict1


def loadAuth():
    with open('auth.json', 'r') as infile:
        return json.load(infile)


def saveAuth(tokenDict):
    with open('auth.json', 'w') as outfile:
        json.dump(tokenDict, outfile)


if __name__ == "__main__":
    pass
