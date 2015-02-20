"""The Event object used by a Schedule"""

# import sys
import datetime

from entry import Entry
from settingsInteraction import settingsInteractionInstance

# JUDGINGTIMEPERENTRY = datetime.timedelta(seconds=60)
# FINALADJUDICATIONTIMEPERENTRY = datetime.timedelta(seconds=180)

class Event(object):
    """Used by a Schedule"""
    def __init__(self, classNumber, className):
        self.classNumber = classNumber
        self.className = className
        self.entries = []
        self.totalTime = datetime.timedelta(seconds=0)

    def calculateTotalTime(self):
        """calculate the total time this Event is likely to take"""
        performanceTime = datetime.timedelta()
        for entry in self.entries:
            performanceTime += entry.totalTime()
        # TODO is the following correct for multiple pieces? Fine for now probably.
        judgingTime = settingsInteractionInstance.loadJudgingTimePerEntry() * len(self.entries)
        finalAdjudicationTime = settingsInteractionInstance.loadFinalAdjudicationTime() * len(self.entries)
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

    def export(self, csvFile, depth=0):
        """Export this event to a csv file as part of the export procedure. \
        csvFile must be a file opened with w permissions.  <depth> empty columns \
        are added to the beginning to serve as indentation"""
        
        leadingCommas = ''
        for _ in range(depth):
            leadingCommas = leadingCommas+','
        
        s = '{indent}{number},"{name}","Total Time: {time}"\n'.format(
            indent=leadingCommas,
            number=self.classNumber,
            name=self.className,
            time=self.totalTime
        )
        csvFile.write(s)
        
        s = '{indent},{header}\n'.format(
            indent=leadingCommas,
            header=Entry.getCsvHeader()
        )
        csvFile.write(s)
        
        for e in self.entries:
            e.export(csvFile, depth+1)

    def toWordFile(self, document):
        """Export to docx for printer, document is from docx module"""
        # Number the entries like 1.
        for i in range(len(self.entries)):
            entry = self.entries[i]
            p = document.add_paragraph("{0}.\t".format(i+1))
            entry.toWordFile(p)
