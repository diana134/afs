"""Unit tests for scheduler.py"""

import sys
sys.path.insert(0, '../')
import unittest

from scheduler import Scheduler, sortEntriesByClass
from entry import Entry

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
    
if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
