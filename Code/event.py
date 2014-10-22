"""The Event object used by a Schedule"""

import sys
import datetime
from entry import Entry

JUDGINGTIMEPERENTRY = datetime.timedelta(seconds=60)
FINALADJUDICATIONTIMEPERENTRY = datetime.timedelta(seconds=180)

def convertTimeToSeconds(timeString):
    """convert MM:SS to seconds"""
    tokens = timeString.split(':')
    return int(tokens[0]) * 60 + int(tokens[1])

def convertStringToTimedelta(timeString):
    """convert 'M:SS' to timedelta"""
    tokens = timeString.split(':')
    minutes = int(tokens[0])
    seconds = int(tokens[1])
    return datetime.timedelta(minutes=minutes, seconds=seconds)

class Event(object):
    """Used by a Schedule"""
    def __init__(self, classNumber):
        self.classNumber = classNumber
        self.className = "" # TODO: is this necessary?
        self.entries = []
        self.totalTime = datetime.timedelta(seconds=0)

    def calculateTotalTime(self):
        """calculate the total time this Event is likely to take"""
        performanceTime = datetime.timedelta()
        for entry in self.entries:
            performanceTime += convertStringToTimedelta(entry.performanceTime)
        judgingTime = JUDGINGTIMEPERENTRY * len(self.entries)
        finalAdjudicationTime = FINALADJUDICATIONTIMEPERENTRY * len(self.entries)
        self.totalTime = performanceTime + judgingTime + finalAdjudicationTime

    def addEntry(self, entry):
        """add an Entry to this Event and recalculate the totalTime"""
        self.entries.append(entry)
        self.calculateTotalTime()

    def getParticipantIds(self):
        """returns a list of the participantIds for the Entries"""
        idList = []
        for entry in self.entries:
            idList.append(entry.participantID)
        return idList

    def export(self, csvFile,depth=1):
        """Export this event to a csv file as part of the export procedure. \
        csvFile must be a file opened with w permissions.  <depth> empty columns \
        are added to the beginning to serve as indentation"""
        
        leadingCommas = ''
        for i in range(depth):
            leadingCommas = leadingCommas+','
        
        s = '{indent}{number},"{name}","Total Time: {time}"\n'.format(
            indent = leadingCommas,
            number = self.classNumber,
            name = self.className,
            time = self.totalTime
        )
        csvFile.write(s)
        
        s = '{indent},{header}\n'.format(
            indent = leadingCommas,
            header = Entry.getCsvHeader()
        )
        csvFile.write(s)
        
        for e in self.entries:
            e.export(csvFile, depth+1)
