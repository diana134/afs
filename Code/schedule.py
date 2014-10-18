"""The Schedule object used by the scheduling algorithm"""

import sys
from random import randrange, shuffle
import datetime

class Schedule(object):
    """Used by the scheduling algorithm"""
    def __init__(self, arrangement=None):
        self.arrangement = arrangement if arrangement is not None else [] # list of [dateTime, Event] lists
        # self.startTime = startTime # datetime object of the time this Schedule should start
        # self.endTime = endTime # datetime object of the time this Schedule should end by
        self.fitness = 0 # closer to 0 is better
        self.feasible = None # decided while calulating fitnes

    @classmethod
    def makeNewRandomSchedule(cls, eventList, scheduleStartDatetime, scheduleEndDatetime):
        """Returns a new random Schedule sorted by start times"""
        arrangement = []
        shuffle(eventList)
        for entry in eventList:
            # Generate a random start time between scheduleStartDatetime and scheduleEndDatetime
            arrangement.append([Schedule.generateStartTimeInIncrements(scheduleStartDatetime, scheduleEndDatetime), entry])
        schedule = Schedule(arrangement=arrangement)
        # Sort the arrangement by start times
        schedule.sort()
        return schedule

    @staticmethod
    def generateStartTimeInIncrements(scheduleStartDatetime, scheduleEndDatetime):
        """Returns a datetime object between scheduleStartDatetime and scheduleEndDatetime in 5 minute increments"""
        # Ensure scheduleEndDate is later than scheduleStartDate
        if scheduleEndDatetime <= scheduleStartDatetime:
            raise Exception("scheduleEndDatetime <= scheduleStartDatetime in Schedule.generateStartTimeInIncrements")
        delta = scheduleEndDatetime - scheduleStartDatetime
        int_delta = delta.total_seconds()
        randomSecond = randrange(0, int_delta, 300)
        return scheduleStartDatetime + datetime.timedelta(seconds=randomSecond)

    def sort(self):
        """Sorts self.arrangement in place in order of start time, ascending"""
        # Magic code from stackoverflow
        self.arrangement.sort(key=lambda tup: tup[0]) 

    def save(self):
        """save this schedule"""
        # As a file? In the DB? Pickle it?
        pass

    def countOverlappingEvents(self):
        """counts the number of overlapping events"""
        overlapCount = 0
        for i in range(len(self.arrangement)):
            # Make sure there is at least one Event left in the arrangement
            if i < len(self.arrangement) - 1:
                time = self.arrangement[i][0]
                event = self.arrangement[i][1]
                nextTime = self.arrangement[i+1][0]
                if time + event.totalTime > nextTime:
                    # events overlap
                    overlapCount += 1
        return overlapCount

    def isStartTimeTooEarly(self, startDateTime):
        """checks if the arrangement starts too early"""
        # TODO is this still useful?
        if self.arrangement[0][0] < startDateTime:
            return True
        else:
            return False

    def isEndTimeTooLate(self, endDateTime):
        """checks if the arrangement ends too late"""
        # TODO is this still useful?
        if self.arrangement[-1][0] + self.arrangement[-1][1].totalTime >= endDateTime:
            return True
        else:
            return False

    def occurancesDuringGivenDatetimes(self, beginDatetime, endDatetime):
        """counts the number of Events that start or end between beginDatetime and endDatetime"""
        occurances = 0
        # Ensure endDatetime is valid
        if endDatetime <= beginDatetime:
            raise Exception("endDatetime <= beginDatetime in Schedule.occurancesDuringGivenDatetimes")
        else:
            for dt, event in self.arrangement:
                # if event starts between beginDatetime and endDatetime
                if dt >= beginDatetime and dt < endDatetime:
                    occurances += 1
                # if event ends between beginDatetime and endDatetime
                elif dt + event.totalTime >= beginDatetime and dt + event.totalTime < endDatetime:
                    occurances += 1
            return occurances

    def occurancesDuringGivenTimes(self, beginTime, endTime):
        """counts the number of Events that start or end between beginTime and endTime"""
        occurances = 0
        # endTime can be before or after beginTime, so figure out which way to count
        if endTime < beginTime:
            # endTime is the next day
            for dt, event in self.arrangement:
                # if event starts between beginTime and endTime
                if dt.time() >= beginTime or dt.time() < endTime:
                    occurances += 1
                # if event ends between beginTime and endTime
                elif (dt + event.totalTime).time() >= beginTime or (dt + event.totalTime).time() < endTime:
                    occurances += 1
        else:
            # endTime is later today
            for dt, event in self.arrangement:
                # if event starts between beginTime and endTime
                if dt.time() >= beginTime and dt.time() < endTime:
                    occurances += 1
                # if event ends between beginTime and endTime
                elif (dt + event.totalTime).time() >= beginTime and (dt + event.totalTime).time() < endTime:
                    occurances += 1
        return occurances

    def countOverbookedSoloParticipants(self):
        """counts the number of times SoloParticipants occur in concsecutive Events"""
        overlapCount = 0
        for i in range(len(self.arrangement) - 1):
            event = self.arrangement[i][1]
            nextEvent = self.arrangement[i+1][1]
            # get participantIds for this event and the next one
            eventParticipants = event.getParticipantIds()
            nextEventParticipants = nextEvent.getParticipantIds()
            # check if any of this Event's Participants are in the next Event too
            for pId in eventParticipants:
                if pId[0] == 's' and pId in nextEventParticipants:
                    overlapCount += 1
        return overlapCount

    def calculateDowntime(self):
        """add up the time when no Events are occurring"""
        downtime = datetime.timedelta(seconds=0)
        for i in range(len(self.arrangement) - 1):
            time = self.arrangement[i][0]
            event = self.arrangement[i][1]
            nextTime = self.arrangement[i+1][0]
            eventEnd = time + event.totalTime
            if eventEnd < nextTime:
                downtime = downtime + (nextTime - eventEnd)
        return downtime

    def calculateFitness(self, scheduleStartDate, scheduleEndDate, lunchStartTime, lunchEndTime, dinnerStartTime, dinnerEndTime, dayStartTime, dayEndTime):
        """assesses the 'goodness' of the arrangement based on participants not being \
        overbooked (constraint), schools being together, and young kids being in the morning(?)"""
        
        scheduleStartDatetime = datetime.datetime.combine(scheduleStartDate, dayStartTime)
        scheduleEndDatetime = datetime.datetime.combine(scheduleEndDate, dayEndTime)

        # Ensure Events do no overlap
        overlapCount = self.countOverlappingEvents()
        if overlapCount > 0:
            # infeasible
            self.feasible = False
            # decrease fitness based on number of overlapping Events
            self.fitness -= overlapCount

        # Ensure arrangement occurs entirely within given dates
        goodOccurances = self.occurancesDuringGivenDatetimes(scheduleStartDatetime, scheduleEndDatetime)
        erroneousOccurances = abs(len(self.arrangement) - goodOccurances)
        if erroneousOccurances > 0:
            # infeasible
            self.feasible = False
            # decrease fitness based on number of Events not occuring within the specified time
            self.fitness -= erroneousOccurances

        # Ensure Events do not begin or end during lunch time
        lunchOccurances = self.occurancesDuringGivenTimes(lunchStartTime, lunchEndTime)
        if lunchOccurances > 0:
            # infeasible
            self.feasible = False
            # decrease fitness based on number of Events occuring during lunch
            self.fitness -= lunchOccurances

        # Ensure Events do not begin or end during dinner time
        dinnerOccurances = self.occurancesDuringGivenTimes(dinnerStartTime, dinnerEndTime)
        if dinnerOccurances > 0:
            # infeasible
            self.feasible = False
            # decrease fitness based on number of Events occuring during dinner
            self.fitness -= dinnerOccurances

        # Ensure Events do not begin or end at night i.e. (between 9pm one night and 9am the next day)
        nightOccurances = self.occurancesDuringGivenTimes(dayEndTime, dayStartTime)
        if nightOccurances > 0:
            # infeasible
            self.feasible = False
            # decrease fitness based on number of Events occuring during the night
            self.fitness -= nightOccurances

        # At this point if feasibility hasn't been marked false, this is a feasible Schedule
        if self.feasible is None:
            self.feasible = True

        # Check if SoloParticipants are in concsecutive Events
        soloParticipantOverlaps = self.countOverbookedSoloParticipants()
        if soloParticipantOverlaps > 0:
            # decrease fitness based on number of solo participant overlaps
            self.fitness -= soloParticipantOverlaps

        # We want a minimum of downtime between Events
        downtime = self.calculateDowntime()
        # Decrease fitness by 1 point for every 5 minutes of downtime
        self.fitness -= downtime.total_seconds() / 300

        # Ensure GroupParticipants from same school are in consecutive events(?)
        # (does not apply to anything with constume changes i.e. Dance, Musical Theatre)

        # Bonus points for Events for young ages being in the morning(?)

        # Bonus points for Events for teens being in the evening(?)
