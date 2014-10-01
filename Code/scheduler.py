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
        self.population = [] # this holds the population of potential schedules
        
    def process(self):
        """The big fancy algorithm"""
        # Get all the entries
        entryList = self.db.getAllEntries()
        # Sort them by class into Events
        eventList = sortEntriesByClass(entryList)
        # Now start making Schedules
        # Initialize the population
        # there are an awful lot of ways the events can be ordered, 
        # so just start with 1000 and see where that gets us
        for _ in xrange(1, 1000):
            self.population.append(Schedule.makeNewRandomSchedule(eventList, startTime, endTime))

        done = False
        while not done:
            # Select individuals for mating
            # Sort population by fitness, descending
            self.population.sort(key=lambda x: x.fitness, reverse=True) # Magic code from stackoverflow
            # Choose top 10% (100 individuals in this case)
            parents = self.population[:len(self.population)*0.1]

            # Mate individuals to produce offspring

            # Mutate offspring

            # Add offspring to population (replace population?)

            # Check if we have a feasible solution
