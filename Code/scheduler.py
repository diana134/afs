"""Contains the scheduling algorithm and all its bits"""

import sys
import random
import datetime

from schedule import Schedule
from event import Event

# MUTATIONRATE = 0.1 # 10% chance of mutation
TOLERANCE = datetime.timedelta(minutes=10)

def sortEntriesByClass(entryList):
    """Sorts entryList into Events by class and returns a list sorted by ascending class number"""
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
    eventList.sort(key=lambda x: x.classNumber, reverse=False) # Magic code from stackoverflow
    return eventList

class Scheduler(object):
    """Handles the scheduling of all the Events"""
    def __init__(self, db):
        self.possibleEvents = []
        # self.db = db
    #     self.population = [] # this holds the population of potential schedules

    # @staticmethod
    # def mate(parents):
    #     """mates each pair of parents and returns a list of offspring"""
    #     offspring = []
    #     for i in xrange(0, len(parents) - 1, 2):
    #         mom = parents[i].arrangement
    #         dad = parents[i+1].arrangement
    #         child1 = []
    #         child2 = []
    #         for j in xrange(len(mom)):
    #             child1Time = None
    #             child1Event = None
    #             child2Time = None
    #             child2Event = None
    #             # Randomly choose which time each child will get
    #             timeChoice = random.randint(0, 1)
    #             if timeChoice == 0:
    #                 # child1 gets mom's time, child2 gets dad's time
    #                 child1Time = mom[j][0]
    #                 child2Time = dad[j][0]
    #             else:
    #                 # child2 gets mom's time, child1 gets dad's time
    #                 child1Time = dad[j][0]
    #                 child2Time = mom[j][0]

    #             # Randomly choose which event each child will get
    #             eventChoice = random.randint(0, 1)
    #             if eventChoice == 0:
    #                 # child1 gets mom's event, child2 gets dad's event
    #                 child1Event = mom[j][1]
    #                 child2Event = dad[j][1]
    #             else:
    #                 # child2 gets mom's event, child1 gets dad's event
    #                 child1Event = dad[j][1]
    #                 child2Event = mom[j][1]

    #             child1.append([child1Time, child1Event])
    #             child2.append([child2Time, child2Event])

    #         # Add the children to the list of offspring
    #         childSched1 = Schedule(child1)
    #         childSched2 = Schedule(child2)
    #         offspring.append(childSched1)
    #         offspring.append(childSched2)
    #     return offspring

    # @staticmethod
    # def mutate(offspring):
    #     """takes a list of Schedules and modifies the start time +/-5 minutes and swaps Events in each"""
    #     for child in offspring:
    #         for i in xrange(len(child.arrangement)):
    #             time, event = child.arrangement[i]
    #             # Will this element mutate?
    #             mutationChance = random.random()
    #             if mutationChance <= MUTATIONRATE:
    #                 # Change time +/- 5 min
    #                 newTime = None
    #                 plusOrMinus = random.random()
    #                 if plusOrMinus < 0.5:
    #                     # Subtract 5 minutes
    #                     newTime = time - datetime.timedelta(minutes=5)
    #                 else:
    #                     # Add 5 minutes
    #                     newTime = time + datetime.timedelta(minutes=5)
    #                 child.arrangement[i][0] = newTime
    #                 # Swap this Event with another
    #                 swapTarget = random.randint(0, len(child.arrangement))
    #                 tmpEvent = event
    #                 child.arrangement[i][1] = child.arrangement[swapTarget][1]
    #                 child.arrangement[swapTarget][1] = tmpEvent
    #     return offspring # necessary? have we modified the original object? python is strange
        
    # def process(self):
    #     """The big fancy algorithm, returns a solution"""

    #     scheduleStartDate = datetime.date(2014, 1, 1)
    #     scheduleEndDate = datetime.date(2014, 1, 1)
    #     dayStartTime = datetime.time(9)
    #     dayEndTime = datetime.time(21)
    #     lunchStartTime = datetime.time(12)
    #     lunchEndTime = datetime.time(13)
    #     dinnerStartTime = datetime.time(17)
    #     dinnerEndTime = datetime.time(18)

    #     scheduleStartDatetime = datetime.datetime.combine(scheduleStartDate, dayStartTime)
    #     scheduleEndDatetime = datetime.datetime.combine(scheduleEndDate, dayEndTime)

    #     solution = None

    #     # Get all the entries
    #     entryList = self.db.getAllEntries()

    #     # Sort them by class into Events
    #     eventList = sortEntriesByClass(entryList)
        
    #     # Initialize the population
    #     # (there are an awful lot of ways the events can be ordered, 
    #     # so just start with 1000 and see where that gets us)
    #     for _ in xrange(1, 1000):
    #         self.population.append(Schedule.makeNewRandomSchedule(eventList, scheduleStartDatetime, scheduleEndDatetime))

    #     done = False
    #     while not done:
    #         # Sort population by fitness, descending
    #         print "Sorting population..."
    #         self.population.sort(key=lambda x: x.fitness, reverse=True) # Magic code from stackoverflow
    #         # Choose top 10% for mating
    #         activeNumber = int(round(len(self.population)*0.1)) # 10% of the population
    #         parents = self.population[:activeNumber]

    #         # Mate parents to produce offspring
    #         print "Mating parents..."
    #         offspring = self.mate(parents)

    #         # Mutate offspring
    #         print "Mutating offspring..."
    #         mutatedOffspring = self.mutate(offspring) # have we modified the original offspring?

    #         # Assess the new Schedules
    #         print "Assessing new schedules..."
    #         for child in mutatedOffspring:
    #             child.calculateFitness(scheduleStartDate, scheduleEndDate, lunchStartTime, lunchEndTime, dinnerStartTime, dinnerEndTime, dayStartTime, dayEndTime)

    #         # Add offspring to population (replace population worst 10%, 
    #         # not caring if any of the offspring are actually worse)
    #         print "Merging offspring into population..."
    #         self.population[-activeNumber:] = mutatedOffspring

    #         # Check if we have a feasible solution
    #         # TODO: do 10 more iterations after finding a solution to see if it gets better
    #         # while retaining this one ?
    #         print "Checking for feasible solution..."
    #         for child in mutatedOffspring:
    #             if child.feasible:
    #                 print "Solution found."
    #                 done = True
    #                 solution = child

    #     return solution


    # TODO pass in and handle all the dates and times
    def process(self, entriesInDiscipline, sessionDatetimes):
        """Starts a backtracking search for a solution, returns a valid Schedule or None if no solution exists"""
        print "Working..."
        schedule = Schedule(sessionDatetimes)
        self.possibleEvents = sortEntriesByClass(entriesInDiscipline)

        result = self.recursiveProcess(schedule)
        print "Finished"
        return result

    def recursiveProcess(self, schedule):
        """Performs a backtracking search for a solution, returns a valid Schedule or None if no solution exists"""
        # Check if there are any more events to add
        if not self.possibleEvents:
            return schedule

        # # select next space to fill
        # session = schedule.findNextFit()

        for event in self.possibleEvents:
            # select next space to fill
            session = schedule.findNextFit(event.totalTime)
            if session is None:
                # can't fit the event in this schedule
                print "can't fit " + event.classNumber + " in schedule"
                return None
            if Scheduler.satisfiesContraints(session, event):
                # add event to the space in schedule
                print "adding event " + event.classNumber + " to session at " + str(session.startDatetime)
                session.add(event)
                self.possibleEvents.remove(event)
                result = self.recursiveProcess(schedule)
                if result is not None:
                    return result
                else:
                    # remove event from space in schedule
                    session.remove(event)
                    self.possibleEvents.append(event)
        print "gone through all events"
        return None

    @staticmethod
    def satisfiesContraints(session, event):
        """Returns true if adding this event to this session is valid"""
        valid = True

        # Check that there is time for this event, within a tolerance
        if event.totalTime > session.emptyTime() + TOLERANCE:
            valid = False

        return valid
