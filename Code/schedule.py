"""The Schedule object used by the scheduling algorithm"""

import sys

class Schedule(object):
    """Used by the scheduling algorithm"""
    def __init__(self):
        self.arrangement = [[]] # [time][Event]
        # TODO have a init that randomly makes an arrangement?

    def fitness(self):
        """assesses the 'goodness' of the arrangement based on participants not being \
        overbooked (constraint), schools being together, and young kids being in the morning(?)"""
        pass