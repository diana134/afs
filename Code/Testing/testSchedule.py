"""Unit tests for schedule.py"""

import sys
sys.path.insert(0, '../')
import unittest

from schedule import Schedule
from event import Event

class CheckForOverlappingEventsTests(unittest.TestCase):
    """tests functions in Schedule"""
    def setUp(self):
        # Make some Events and fudge the totalTime
        self.e1 = Event("1")
        self.e1.totalTime = 10
        self.e2 = Event("2")
        self.e2.totalTime = 10
        self.e3 = Event("3")
        self.e3.totalTime = 10
    
    def testNoOverlaps(self):
        """test that no overlapping Events returns 0"""
        # Make a Schedule with non-overlapping times
        s = Schedule()
        s.arrangement.append((0, self.e1))
        s.arrangement.append((20, self.e2))
        s.arrangement.append((40, self.e3))
        # Now the actual test
        count = s.checkForOverlappingEvents()
        self.assertEqual(count, 0)

    def testOverlapsOnStartEndTimes(self):
        """test that overlaps occur when an Event starts when the previous one ends"""
        # Make a Schedule with overlapping times
        s = Schedule()
        s.arrangement.append((0, self.e1))
        s.arrangement.append((10, self.e2))
        s.arrangement.append((20, self.e3))
        # Now the actual test
        count = s.checkForOverlappingEvents()
        self.assertEqual(count, 2)

    def testOverlapsOnSameStartTime(self):
        """test that overlaps are counted properly when events start at the same time"""
        # Make a Schedule with same times
        s = Schedule()
        s.arrangement.append((0, self.e1))
        s.arrangement.append((0, self.e2))
        s.arrangement.append((0, self.e3))
        # Now the actual test
        count = s.checkForOverlappingEvents()
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
