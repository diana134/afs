"""Unit tests for event.py"""

import sys
sys.path.insert(0, '../')
import unittest
import datetime

from event import Event, JUDGINGTIMEPERENTRY, FINALADJUDICATIONTIMEPERENTRY
from entry import Entry

class EventTests(unittest.TestCase):
    """tests the functions of an Event"""
    def setUp(self):
        # Create an Event with a class number but no Entries
        self.testEvent = Event("T4242")

    def testCalculateTotalTimeNoEntries(self):
        """test that an Event with no Entries has a total time of 0"""
        self.testEvent.calculateTotalTime()
        self.assertEqual(self.testEvent.totalTime, datetime.timedelta())
    
    def testAddEntry(self):
        """test that adding an Entry correctly updates the totalTime"""
        entry = Entry(0, 0, "Test", 0, "T4242", "Test Class", "Foo Bar", "1:00")
        self.testEvent.addEntry(entry)
        timeShouldBe = datetime.timedelta(minutes=1) + JUDGINGTIMEPERENTRY + FINALADJUDICATIONTIMEPERENTRY
        self.assertEqual(self.testEvent.totalTime, timeShouldBe)

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
