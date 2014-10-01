"""Contains the scheduling algorithm and all its bits"""

import sys
import random

from schedule import Schedule
from event import Event

MUTATIONRATE = 0.25 # 25% chance of mutation

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

    @staticmethod
    def mate(parents):
        """mates each pair of parents and returns a list of offspring"""
        offspring = []
        for i in xrange(0, len(parents) - 1, 2):
            mom = parents[i].arrangement
            dad = parents[i+1].arrangement
            child1 = []
            child2 = []
            for j in xrange(len(mom)):
                child1Time = None
                child1Event = None
                child2Time = None
                child2Event = None
                # Randomly choose which time each child will get
                timeChoice = random.randint(0, 1)
                if timeChoice == 0:
                    # child1 gets mom's time, child2 gets dad's time
                    child1Time = mom[j][0]
                    child2Time = dad[j][0]
                else:
                    # child2 gets mom's time, child1 gets dad's time
                    child1Time = dad[j][0]
                    child2Time = mom[j][0]

                # Randomly choose which event each child will get
                eventChoice = random.randint(0, 1)
                if eventChoice == 0:
                    # child1 gets mom's event, child2 gets dad's event
                    child1Event = mom[j][1]
                    child2Event = dad[j][1]
                else:
                    # child2 gets mom's event, child1 gets dad's event
                    child1Event = dad[j][1]
                    child2Event = mom[j][1]

                child1.append([child1Time, child1Event])
                child2.append([child2Time, child2Event])

            # Add the children to the list of offspring
            childSched1 = Schedule(child1)
            childSched2 = Schedule(child2)
            offspring.append(childSched1)
            offspring.append(childSched2)
        return offspring

    # @staticmethod
    # def mutate(offspring):
    #     """modify the start time +/- 5 minutes and swap Events in each offspring"""
    #     for child in offspring:
    #         for i in xrange(len(child.arrangement)):
    #             time, event = child.arrangement[i]
    #             newTime = None
    #             # Will this element mutate?
    #             mutationChance = random.random()
    #             if mutationChance <= MUTATIONRATE:
    #                 # Change time +/- 5 min
    #                 plusOrMinus = random.random()
    #                 if plusOrMinus < 0.5:
    #                     # Subtract 5 minutes
    #                     newTime = time - datetime.timedelta(minutes=5)
    #                 else:
    #                     # Add 5 minutes
    #                     newTime = time + datetime.timedelta(minutes=5)
        
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
            # Sort population by fitness, descending
            self.population.sort(key=lambda x: x.fitness, reverse=True) # Magic code from stackoverflow
            # Choose top 10% for mating
            parents = self.population[:len(self.population)*0.1]

            # Mate parents to produce offspring
            offspring = self.mate(parents)

            # Mutate offspring
            # mutatedOffspring = self.mutate(offspring)

            # Add offspring to population (replace population?)

            # Check if we have a feasible solution
