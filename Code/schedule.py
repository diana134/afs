"""The Schedule object used by the scheduling algorithm"""

import sys

class Schedule(object):
    """Used by the scheduling algorithm"""
    def __init__(self):
        self.arrangement = [] # list of (dateTime, Event) tuples (remember that these are immutable)
        # TODO: time can only change +/- 5 minutes (300 seconds)
        # TODO have a init that randomly makes an arrangement?

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
                if time + event.totalTime >= nextTime:
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

    def occurancesDuringGivenTimes(self, beginTime, endTime):
        """counts the number of Events that start or finish between beginTime and endTime"""
        occurances = 0
        # Ensure endTime is later than beginTime
        if endTime <= beginTime:
            raise Exception("endTime <= beginTime in Schedule.occursDuringGivenTime")
        else:
            for time, event in self.arrangement:
                # if event starts between beginTime and endTime
                if time >= beginTime and time < endTime:
                    occurances += 1
                # if event ends between beginTime and endTime
                elif time + event.totalTime >= beginTime and time + event.totalTime < endTime:
                    occurances += 1
            return occurances

    def countOverbookedSoloParticipants(self):
        """counts the number of times SoloParticipants occur in concsecutive Events"""
        overlapCount = 0
        for i in range(len(self.arrangement)):
            # Make sure there is at least one Event left in the arrangement
            if i < len(self.arrangement) - 1:
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

    def fitness(self):
        """assesses the 'goodness' of the arrangement based on participants not being \
        overbooked (constraint), schools being together, and young kids being in the morning(?)"""
        # TODO: make sure arrangement is sorted by time before beginning
        
        # Ensure Events do no overlap
        overlapCount = self.countOverlappingEvents()
        if overlapCount > 0:
            # mark as infeasible
            # decrease fitness based on number of overlapping Events
            pass

        # Ensure arrangement occurs entirely within given times
        startDateTime = None # TODO: where does this come from?
        endDateTime = None
        goodOccurances = self.occurancesDuringGivenTimes(startDateTime, endDateTime)
        erroneousOccurances = abs(len(self.arrangement) - goodOccurances)
        if erroneousOccurances > 0:
            # Mark as infeasible
            # decrease fitness based on number of Events not occuring within the specified time
            pass

        # Ensure Events do not begin or end during lunch time
        lunchStartTime = None
        lunchEndTime = None
        lunchOccurances = self.occurancesDuringGivenTimes(lunchStartTime, lunchEndTime)
        if lunchOccurances > 0:
            # Mark as infeasible
            # decrease fitness based on number of Events occuring during lunch
            pass

        # Ensure Events do not begin or end during dinner time
        dinnerStartTime = None
        dinnerEndTime = None
        dinnerOccurances = self.occurancesDuringGivenTimes(dinnerStartTime, dinnerEndTime)
        if dinnerOccurances > 0:
            # Mark as infeasible
            # decrease fitness based on number of Events occuring during dinner
            pass

        # Ensure Events do not begin or end at night i.e. (between 9pm one night and 9am the next day)
        dayEndTime = None
        nextDayStartTime = None
        nightOccurances = self.occurancesDuringGivenTimes(dayEndTime, nextDayStartTime)
        if nightOccurances > 0:
            # Mark as infeasible
            # decrease fitness based on number of Events occuring during the night
            pass

        # Ensure SoloParticipants are not in concsecutive Events
        soloParticipantOverlaps = self.countOverbookedSoloParticipants()
        if soloParticipantOverlaps > 0:
            # Mark as infeasible
            # decrease fitness based on number of solo participant overlaps
            pass

        # Ensure GroupParticipants from same school are in consecutive events(?)
        # (does not apply to anything with constume changes i.e. Dance, Musical Theatre)

        # Bonus points for Events for young ages being in the morning(?)

        # Bonus points for Events for teens being in the evening(?)
