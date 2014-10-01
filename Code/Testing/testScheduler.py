"""Unit tests for scheduler.py"""

import sys
sys.path.insert(0, '../')
import unittest
import datetime

from scheduler import Scheduler, sortEntriesByClass
from entry import Entry
from event import Event
from schedule import Schedule

class ShedulerTests(unittest.TestCase):
    """tests the helper functions in Scheduler"""
    
    def testSortEntriesByClass(self):
        """test that this sorts things properly"""
        e1 = Entry(classNumber="T1", performanceTime="1:20")
        e2 = Entry(classNumber="T1", performanceTime="2:10")

        e3 = Entry(classNumber="T2", performanceTime="0:42")

        e4 = Entry(classNumber="T3", performanceTime="0:01")

        eventList = sortEntriesByClass([e1, e3, e4, e2])
        self.assertTrue(len(eventList) == 3)
        self.assertTrue(len(eventList[0].entries) == 2)
        self.assertTrue(len(eventList[1].entries) == 1)
        self.assertTrue(len(eventList[2].entries) == 1)

class MateTests(unittest.TestCase):    
    """tests for MateTests"""
    
    def testSanity(self):
        """4 identical parents should produce 4 identical offspring"""
        startTime = datetime.datetime(2014, 1, 1, 1)
        event = Event("1")
        parent = Schedule([(startTime, event)])
        parents = [parent, parent, parent, parent]
        # Mate to produce offspring
        offspring = Scheduler.mate(parents)
        # Make sure there are 4 offspring
        self.assertEqual(len(offspring), 4)
        # Make sure all offspring == parent
        for child in offspring:
            self.assertEqual(child.arrangement, parent.arrangement)
    
if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
