"""Unit tests for schedule.py"""

import sys
sys.path.insert(0, '../')
import unittest
import datetime

from schedule import Schedule
from event import Event

class CountOverlappingEventsTests(unittest.TestCase):
    """tests countOverlappingEvents"""
    def setUp(self):
        # Make some Events and fudge the totalTime
        self.e1 = Event("1")
        self.e1.totalTime = datetime.timedelta(minutes=1)
        self.e2 = Event("2")
        self.e2.totalTime = datetime.timedelta(minutes=1)
        self.e3 = Event("3")
        self.e3.totalTime = datetime.timedelta(minutes=1)
    
    def testNoOverlaps(self):
        """test that no overlapping Events returns 0"""
        # Make a Schedule with non-overlapping times
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0), self.e1))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 2), self.e2))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 4), self.e3))
        # Now the actual test
        count = s.countOverlappingEvents()
        self.assertEqual(count, 0)

    def testOverlapsOnStartEndTimes(self):
        """test that overlaps occur when an Event starts when the previous one ends"""
        # Make a Schedule with overlapping times
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0), self.e1))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 1), self.e2))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 2), self.e3))
        # Now the actual test
        count = s.countOverlappingEvents()
        self.assertEqual(count, 2)

    def testOverlapsOnSameStartTime(self):
        """test that overlaps are counted properly when events start at the same time"""
        # Make a Schedule with same times
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0), self.e1))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0), self.e2))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0), self.e3))
        # Now the actual test
        count = s.countOverlappingEvents()
        self.assertEqual(count, 2)

class IsStartTimeTooEarlyTests(unittest.TestCase):
    """tests IsStartTimeTooEarly"""
    def setUp(self):
        # Make an Event and fudge the totalTime
        self.e1 = Event("1")
        self.e1.totalTime = datetime.timedelta(minutes=1)

    def testEarlyTimeIsTrue(self):
        """a too early start time returns true"""
        # Make a Schedule
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 8, 0, 0), self.e1))
        # Make a startDateTime later than the first Event
        startDateTime = datetime.datetime(2014, 1, 1, 9, 0, 0)
        # Test
        self.assertTrue(s.isStartTimeTooEarly(startDateTime))

    def testOnTimeIsFalse(self):
        """an on time start time returns false"""
        # Make a Schedule
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0, 0), self.e1))
        # Make a startDateTime the same time as the first Event
        startDateTime = datetime.datetime(2014, 1, 1, 9, 0, 0)
        # Test
        self.assertFalse(s.isStartTimeTooEarly(startDateTime))

    def testLateTimeIsFalse(self):
        """a late start time returns false"""
        # Make a Schedule
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 10, 0, 0), self.e1))
        # Make a startDateTime earlier than the first Event
        startDateTime = datetime.datetime(2014, 1, 1, 9, 0, 0)
        # Test
        self.assertFalse(s.isStartTimeTooEarly(startDateTime))

class IsEndTimeTooLateTests(unittest.TestCase):
    """tests IsEndTimeTooLate"""
    def setUp(self):
        # Make an Event and fudge the totalTime
        self.e1 = Event("1")
        self.e1.totalTime = datetime.timedelta(minutes=1)

    def testEarlyTimeIsFalse(self):
        """an early end time returns false"""
        # Make a Schedule
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 20, 0, 0), self.e1))
        # Make a startDateTime later than the last Event ends
        endDateTime = datetime.datetime(2014, 1, 1, 21, 0, 0)
        # Test
        self.assertFalse(s.isEndTimeTooLate(endDateTime))

    def testOnTimeIsTrue(self):
        """an on time end time returns true"""
        # Make a Schedule
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 20, 59, 0), self.e1))
        # Make a startDateTime the same time as the last Event ends
        endDateTime = datetime.datetime(2014, 1, 1, 21, 0, 0)
        # Test
        self.assertTrue(s.isEndTimeTooLate(endDateTime))

    def testLateTimeIsTrue(self):
        """a late end time returns true"""
        # Make a Schedule
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 22, 0, 0), self.e1))
        # Make a endDateTime earlier than the last Event
        endDateTime = datetime.datetime(2014, 1, 1, 21, 0, 0)
        # Test
        self.assertTrue(s.isEndTimeTooLate(endDateTime))

class OccurancesDuringGivenTimesTests(unittest.TestCase):
    """tests occurancesDuringGivenTimes"""
    def setUp(self):
        # Make some Events and fudge the totalTime
        self.e1 = Event("1")
        self.e1.totalTime = datetime.timedelta(minutes=1)
        self.e2 = Event("2")
        self.e2.totalTime = datetime.timedelta(minutes=1)
        self.e3 = Event("3")
        self.e3.totalTime = datetime.timedelta(minutes=1)
        # Make a Schedule
        self.s = Schedule()
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 0, 0), self.e1))
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 2, 0, 0), self.e2))
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 3, 0, 0), self.e3))

    def testEndTimeBeforeBeginTimeRaisesException(self):
        """having endTime >= beginTime should raise an exception"""
        beginTime = datetime.datetime(2014, 1, 1, 5)
        endTime = datetime.datetime(2014, 1, 1, 1)
        self.assertRaises(Exception, self.s.occurancesDuringGivenTimes, beginTime, endTime)

    def testEventsEndBefore(self):
        """all Events start and end before beginTime should return 0"""
        # Make beginTime after all Events are over
        beginTime = datetime.datetime(2014, 1, 1, 4)
        endTime = datetime.datetime(2014, 1, 1, 5)
        # Test
        self.assertEqual(self.s.occurancesDuringGivenTimes(beginTime, endTime), 0)

    def testEventSpanningBegin(self):
        """an Event spanning beginTime should return 1"""
        # Make beginTime during e2
        beginTime = datetime.datetime(2014, 1, 1, 2, 0, 30)
        endTime = datetime.datetime(2014, 1, 1, 3)
        # Test
        self.assertEqual(self.s.occurancesDuringGivenTimes(beginTime, endTime), 1)

    def testEventDuringTime(self):
        """an Event during beginTime and endTime should return only 1"""
        # Make beginTime before e2 and endTime after e2
        beginTime = datetime.datetime(2014, 1, 1, 1, 2, 0)
        endTime = datetime.datetime(2014, 1, 1, 2, 2, 0)
        # Test
        self.assertEqual(self.s.occurancesDuringGivenTimes(beginTime, endTime), 1)

    def testEventSpanningEnd(self):
        """an Event spanning endTime should return 1"""
        # Make endTime during e2
        beginTime = datetime.datetime(2014, 1, 1, 1, 2)
        endTime = datetime.datetime(2014, 1, 1, 2, 0, 30)
        # Test
        self.assertEqual(self.s.occurancesDuringGivenTimes(beginTime, endTime), 1)

    def testEventsBeginAfter(self):
        """all Events start and end after endTime should return 0"""
        # Make endTime before all events occur
        beginTime = datetime.datetime(2014, 1, 1, 0)
        endTime = datetime.datetime(2014, 1, 1, 0, 1)
        # Test
        self.assertEqual(self.s.occurancesDuringGivenTimes(beginTime, endTime), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results