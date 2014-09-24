"""Unit tests for event.py"""

import sys
sys.path.insert(0, '../')
import unittest

from event import Event
from entry import Entry

class EventTests(unittest.TestCase):
    """tests the functions of an Event"""
    def setUp(self):
        self.testEvent = Event("T4242")

    def testCalculateTotalTimeNoEntries(self):
        """test that an Event with no Entries has totalTime == 0"""
        self.testEvent.calculateTotalTime()
        self.assertTrue(self.testEvent.totalTime == 0)
    
    def testAddEntry(self):
        """test that adding an Entry correctly updates the totalTime"""
        entry = Entry(0, 0, "Test", 0, "T4242", "Test Class", "Foo Bar", "1:00")
        self.testEvent.addEntry(entry)
        self.assertTrue(self.testEvent.totalTime == 300)

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
