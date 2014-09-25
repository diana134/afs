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

    def checkForOverlappingEvents(self):
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
        if self.arrangement[0][0] < startDateTime:
            return True
        else:
            return False

    def isEndTimeTooLate(self, endDateTime):
        """checks if the arrangement ends too late"""
        if self.arrangement[-1][0] + self.arrangement[-1][1].totalTime >= endDateTime:
            return True
        else:
            return False

    def occursDuringGivenTime(self, beginTime, endTime):
        """checks if any of the Events in the arrangement have start or \
        end times that are between beginTime and endTime"""
        # Ensure endTime is later than beginTime
        if endTime <= beginTime:
            raise Exception("endTime <= beginTime in Schedule.occursDuringGivenTime")
        else:
            for time, event in self.arrangement:
                # if event starts between beginTime and endTime
                if time >= beginTime and time < endTime:
                    return True
                # if event ends between beginTime and endTime
                if time + event.totalTime >= beginTime and time + event.totalTime < endTime:
                    return True
            # if we made it here, nothing started or ended between beginTime and endTime
            return False

    def fitness(self):
        """assesses the 'goodness' of the arrangement based on participants not being \
        overbooked (constraint), schools being together, and young kids being in the morning(?)"""
        # TODO: make sure arrangement is sorted by time before beginning
        
        # Ensure Events do no overlap
        overlapCount = self.checkForOverlappingEvents()
        # TODO: if overlapCount > 0 mark as infeasible
        # TODO: decrease fitness based on number of overlapping Events

        # Ensure arrangement does not begin before the start date/time
        startDateTime = None # TODO: where does this come from?
        if self.isStartTimeTooEarly(startDateTime):
            # Mark as infeasible
            # decrease fitness
            pass
        else:
            # increase fitness
            pass

        # Ensure arrangement does not end after end date/time
        endDateTime = None # TODO: where does this come from?
        if self.isEndTimeTooLate(endDateTime):
            # Mark as infeasible
            # decrease fitness
            pass
        else:
            # increase fitness
            pass

        # Ensure Events do not begin or end during lunch time
        lunchStartTime = None
        lunchEndTime = None
        if self.occursDuringGivenTime(lunchStartTime, lunchEndTime):
            # Mark as infeasible
            # decrease fitness
            pass
        else:
            # increase fitness
            pass

        # Ensure Events do not begin or end during dinner time
        dinnerStartTime = None
        dinnerEndTime = None
        if self.occursDuringGivenTime(dinnerStartTime, dinnerEndTime):
            # Mark as infeasible
            # decrease fitness
            pass
        else:
            # increase fitness
            pass

        # Ensure Events do not begin or end at night i.e. (between 9pm one night and 9am the next day)
        dayEndTime = None
        nextDayStartTime = None
        if self.occursDuringGivenTime(dayEndTime, nextDayStartTime):
            # Mark as infeasible
            # decrease fitness
            pass
        else:
            # increase fitness
            pass

        # Ensure SoloParticipants are not in concsecutive Events

        # Ensure GroupParticipants from same school are in consecutive events
        # (does not apply to anything with constume changes i.e. Dance, Musical Theatre)

        # Bonus points for Events for young ages being in the morning(?)

        # Bonus points for Events for teens being in the evening(?)
