"""The Schedule object used by the scheduling algorithm"""

import sys

class Schedule(object):
    """Used by the scheduling algorithm"""
    def __init__(self):
        self.arrangement = [] # list of (time, Event) tuples (remember that these are immutable)
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

    def fitness(self):
        """assesses the 'goodness' of the arrangement based on participants not being \
        overbooked (constraint), schools being together, and young kids being in the morning(?)"""
        # Note: make sure arrangement is sorted by time before beginning
        
        # Ensure Events do no overlap
        overlapCount = self.checkForOverlappingEvents()
        # TODO: decrease fitness based on number of overlapping Events

        # Ensure Events do not begin or end during meals

        # Ensure Events are over by a certain time (usually 9pm)

        # Ensure SoloParticipants are not in concsecutive Events

        # Ensure GroupParticipants from same school are in consecutive events
        # (does not apply to anything with constume changes i.e. Dance, Musical Theatre)

        # Bonus points for Events for young ages being in the morning(?)

        # Bonus points for Events for teens being in the evening(?)
