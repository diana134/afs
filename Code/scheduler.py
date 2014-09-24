"""Contains the scheduling algorithm and all its bits"""

import sys

from schedule import Schedule
from event import Event

def sortEntriesByClass(entryList):
    """Sorts entryList into Events by class and returns a list"""
    eventList = []
    for entry in entryList:
        for event in eventList:
            if event.classNumber == entry.classNumber:
                event.addEntry(entry)
                break
        else:
            # if we get here, there was no Event for that classNumber, so make one
            newEvent = Event(entry.classNumber)
            newEvent.addEntry(entry)
            eventList.append(newEvent)
    return eventList

class Scheduler(object):
    """Handles the scheduling of all the Events"""
    def __init__(self, db):
        self.db = db
        
    def process(self):
        """The big fancy algorithm"""
        # Get all the entries
        entryList = self.db.getAllEntries()
        # Sort them by class into Events
        eventList = sortEntriesByClass(entryList)
        # Now start making Schedules
        # Initialize the population

        done = False
        while not done:
            pass
            # Select individuals for mating

            # Mate individuals to produce offspring

            # Mutate offspring

            # Add offspring to population (replace population?)

            # Check if we have a feasible solution
