"""The Event object used by a Schedule"""

import sys

JUDGINGTIMEPERENTRY = 60 # seconds
FINALADJUDICATIONTIMEPERENTRY = 180 # seconds

def convertTimeToSeconds(timeString):
    """convert MM:SS to seconds"""
    tokens = timeString.split(':')
    return int(tokens[0]) * 60 + int(tokens[1])

class Event(object):
    """Used by a Schedule"""
    def __init__(self, classNumber):
        self.classNumber = classNumber
        self.className = "" # TODO: is this necessary?
        self.entries = []
        self.totalTime = 0 # in seconds

    def calculateTotalTime(self):
        """calculate the total time this Event is likely to take"""
        performanceTime = 0
        for entry in self.entries:
            timeInSeconds = convertTimeToSeconds(entry.performanceTime)
            performanceTime += timeInSeconds
        judgingTime = len(self.entries) * JUDGINGTIMEPERENTRY
        finalAdjudicationTime = len(self.entries) * FINALADJUDICATIONTIMEPERENTRY
        self.totalTime = performanceTime + judgingTime + finalAdjudicationTime

    def addEntry(self, entry):
        """add an Entry to this Event and recalculate the totalTime"""
        self.entries.append(entry)
        self.calculateTotalTime()
