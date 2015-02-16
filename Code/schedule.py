"""The Schedule object used by the scheduling algorithm"""

import sys
# from random import randrange, shuffle
import datetime
import pickle
from docx import Document

class Session(object):
    """Part of a Schedule"""
    def __init__(self, startDatetime=None, endDatetime=None):
        self.startDatetime = startDatetime
        self.endDatetime = endDatetime
        self.eventList = []

    def add(self, event):
        """Add an event to this session"""
        self.eventList.append(event)

    def remove(self, event):
        """Remove an event from this session"""
        self.eventList.remove(event)

    def filledTime(self):
        """Returns how much time is filled by the events"""
        filledTime = datetime.timedelta()
        for event in self.eventList:
            filledTime += event.totalTime
        return filledTime

    def emptyTime(self):
        """Returns how much empty time there is, will be negative if events go overtime"""
        totalTime = self.endDatetime - self.startDatetime
        emptyTime = totalTime - self.filledTime()
        return emptyTime

    def isFull(self):
        """Returns True if there is no more empty time"""
        if self.emptyTime().total_seconds() == 0:
            return True
        else:
            return False

    def hasTime(self, durationToFit):
        """Returns True if there is sufficient empty time to fit durationToFit"""
        if self.emptyTime() >= durationToFit:
            return True
        else:
            return False
            
    def export(self, csvFile):
        """Export this session to a csv.  The csvFile parameter must be a file with write permissions"""
        s = '"{startDate}","{endDate}","{numEvents} events"\n'.format(
            startDate=self.startDatetime.strftime('%Y/%M/%d %I:%M %p'),
            endDate=self.endDatetime.strftime('%Y/%M/%d %I:%M %p'),
            numEvents=len(self.eventList)
        )
        csvFile.write(s)
        for i in range(len(self.eventList)):
            e = self.eventList[i]
            csvFile.write('Event {n},'.format(n=i+1))
            e.export(csvFile)

    def toWordFile(self, document):
        """Create a docx for the printer, document parameter from docx module"""
        s = "{0}\n".format(self.startDatetime.strftime('%A, %B %d, %Y %I:%M %p'))
        p = document.add_paragraph()
        r = p.add_run(s)
        r.bold = True
        r.caps = True
        for event in self.eventList:
            eventTitle = "{0}\t{1}".format(event.classNumber, event.className)
            p = document.add_paragraph()
            p.add_run(eventTitle).bold = True
            event.toWordFile(document)

class Schedule(object):
    """Used by the scheduling algorithm"""
    def __init__(self, sessionDatetimes=None):
        self.sessions = []
        if sessionDatetimes is not None:
            for startDatetime, endDatetime in sessionDatetimes:
                self.sessions.append(Session(startDatetime, endDatetime))

    def findNextFit(self, durationToFit):
        """Returns the chronologically first session that isn't full, or None if they're all full"""
        # sort sessions ascending
        self.sessions.sort(key=lambda x: x.startDatetime)
        for session in self.sessions:
            print "trying to fit " + str(durationToFit) + " in session with emptyTime = " + str(session.emptyTime())
            if session.hasTime(durationToFit):
                return session
        return None

    def findWorstFit(self):
        """Returns the chronologically first session with the most empty time"""
        # Note: by its nature, this will put younger kids at the beginning of *each* day
        worstFitSession = None
        worstFitTime = datetime.timedelta()
        # sort sessions ascending
        self.sessions.sort(key=lambda x: x.startDatetime)
        for session in self.sessions:
            if session.emptyTime() > worstFitTime:
                worstFitSession = session
                worstFitTime = session.emptyTime()
        return worstFitSession

    def __str__(self):
        """Returns the string representation"""
        s = ""
        # sort sessions ascending by startDatetime
        self.sessions.sort(key=lambda x: x.startDatetime)
        for session in self.sessions:
            s = s + str(session.startDatetime) + '\n'
            for event in session.eventList:
                s = s + '\t' + event.classNumber + '\t' + event.className + '\n'
        return s

    def save(self, filename):
        """Save the schedule as a pickled blob and write it to the specified filename"""
        fout = open(filename, 'w')
        pickle.dump(self, fout)
        fout.close()
        
    def load(self, filename):
        """Load the schedule from a pickled blob"""
        fin = open(filename, 'r')
        loaded = pickle.load(fin)
        fin.close()
        
        # copy the data we loaded into self
        self.sessions = []
        for s in loaded.sessions:
            self.sessions.append(s)
            
    def export(self, filename):
        """Export the schedule as a reasonably-nicely formatted .csv file so they can play around with in in Excel"""
        fout = open(filename, 'w')
        for s in self.sessions:
            s.export(fout)
        fout.close()

    def toWordFile(self, filename):
        """Format schedule as a docx to send to the printer"""
        document = Document()
        p = document.add_paragraph()
        discipline = self.sessions[0].eventList[0].entries[0].discipline
        p.add_run(discipline.upper() + " - ##venue##\n").bold = True
        p.add_run("Adjudicator - ##adjudicator##\n").bold = True
        for s in self.sessions:
            s.toWordFile(document)
        document.save(filename)
