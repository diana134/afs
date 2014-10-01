"""Unit tests for schedule.py"""

import sys
sys.path.insert(0, '../')
import unittest
import datetime

from schedule import Schedule
from event import Event
from entry import Entry

class MakeNewRandomScheduleTests(unittest.TestCase):
    """tests for MakeNewRandomScheduleTests"""

    def testFactory(self):
        """test that the factory method generates a new Schedule with times and Events"""
        startTime = datetime.datetime(2014, 1, 1, 12)
        endTime = datetime.datetime(2014, 1, 1, 13)
        eventList = [Event("1"), Event("2"), Event("3")]
        s = Schedule.makeNewRandomSchedule(eventList, startTime, endTime)
        # Make sure all Events were added
        self.assertEqual(len(s.arrangement), 3)
        # Make sure all Events have times
        for pair in s.arrangement:
            self.assertIsNotNone(pair[0])
        # Make sure the times are sorted
        for i in range(len(s.arrangement) - 1):
            time = s.arrangement[i][0]
            nextTime = s.arrangement[i+1][0]
            self.assertLessEqual(time, nextTime)
    
class GenerateStartTimeInIncrements(unittest.TestCase):
    """tests for GenerateStartTimeInIncrements"""
    
    def testSameStartEnd(self):
        """test that the same start and end times throws an exception"""
        startTime = datetime.datetime(2014, 1, 1, 12)
        endTime = datetime.datetime(2014, 1, 1, 12)
        self.assertRaises(Exception, Schedule.generateStartTimeInIncrements, startTime, endTime)

    def testEndBeforeStart(self):
        """test that an end time before the start time throws an exception"""
        startTime = datetime.datetime(2014, 1, 1, 12)
        endTime = datetime.datetime(2014, 1, 1, 11)
        self.assertRaises(Exception, Schedule.generateStartTimeInIncrements, startTime, endTime)

    def testProperRounding(self):
        """test that given times 10 minutes apart, only 3 results are possible"""
        startTime = datetime.datetime(2014, 1, 1, 12)
        endTime = datetime.datetime(2014, 1, 1, 12, 10)
        possibleResults = [datetime.datetime(2014, 1, 1, 12), datetime.datetime(2014, 1, 1, 12, 5), 
            datetime.datetime(2014, 1, 1, 12, 10)]
        # Try 10 times
        for _ in xrange(1, 10):
            time = Schedule.generateStartTimeInIncrements(startTime, endTime)
            self.assertIn(time, possibleResults)

class Sort(unittest.TestCase):
    """test for Sort"""
    def setUp(self):
        # Make a Schedule
        self.s = Schedule()
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 3), Event("1")))
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 2), Event("2")))
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 1), Event("3")))

    def testSortWorks(self):
        """test that each time is <= the next time"""
        self.s.sort()
        for i in range(len(self.s.arrangement) - 1):
            time = self.s.arrangement[i][0]
            nextTime = self.s.arrangement[i+1][0]
            self.assertLessEqual(time, nextTime)

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

    # No good if we want a minimum of downtime between events
    # def testOverlapsOnStartEndTimes(self):
    #     """test that overlaps occur when an Event starts when the previous one ends"""
    #     # Make a Schedule with overlapping times
    #     s = Schedule()
    #     s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 0), self.e1))
    #     s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 1), self.e2))
    #     s.arrangement.append((datetime.datetime(2014, 1, 1, 9, 2), self.e3))
    #     # Now the actual test
    #     count = s.countOverlappingEvents()
    #     self.assertEqual(count, 2)

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

class CountOverbookedSoloParticipantsTests(unittest.TestCase):
    """tests for CountOverbookedSoloParticipantsTests"""
    def setUp(self):
        # Make some Events
        self.event1 = Event("1")
        self.event2 = Event("2")
        self.event3 = Event("3")
        # Make a Schedule
        self.s = Schedule()
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 0, 0), self.event1))
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 2, 0, 0), self.event2))
        self.s.arrangement.append((datetime.datetime(2014, 1, 1, 3, 0, 0), self.event3))
        # Make some Entries with different particpants
        self.entry1 = Entry(participantID="s1", performanceTime="1:00")
        self.entry2 = Entry(participantID="g2", performanceTime="1:00")
        self.entry3 = Entry(participantID="g3", performanceTime="1:00")

    def testAllEventsHaveSameParticipant(self):
        """should return 2"""
        # Give all the Events an Entry with the same ParticipantID
        self.event1.addEntry(self.entry1)
        self.event2.addEntry(self.entry1)
        self.event3.addEntry(self.entry1)
        # Test
        self.assertEqual(self.s.countOverbookedSoloParticipants(), 2)

    def testConsecutiveEventsHaveSameParticipant(self):
        """should return 1"""
        # Give 2 consecutive Events an Entry with the same ParticipantID
        self.event1.addEntry(self.entry1)
        self.event2.addEntry(self.entry1)
        self.event3.addEntry(self.entry2)
        # for thing in self.s.arrangement:
        #     print thing
        # Test
        self.assertEqual(self.s.countOverbookedSoloParticipants(), 1)

    def testParticipantSeparatedByEvent(self):
        """should return 0"""
        # Give all the outside Events the same Participant
        self.event1.addEntry(self.entry1)
        self.event2.addEntry(self.entry2)
        self.event3.addEntry(self.entry1)
        # Test
        self.assertEqual(self.s.countOverbookedSoloParticipants(), 0)

    def testAllEventsHaveDifferntParticipants(self):
        """should return 0"""
        # Give all the Events a differnt participant
        self.event1.addEntry(self.entry1)
        self.event2.addEntry(self.entry2)
        self.event3.addEntry(self.entry3)
        # Test
        self.assertEqual(self.s.countOverbookedSoloParticipants(), 0)

    def testGroupParticipantsNotCounted(self):
        """should return 0"""
        # Give 2 consecutive events the same GroupParticipant
        self.event1.addEntry(self.entry1)
        self.event2.addEntry(self.entry2)
        self.event3.addEntry(self.entry2)
        # Test
        self.assertEqual(self.s.countOverbookedSoloParticipants(), 0)

class CalculateDowntimeTests(unittest.TestCase):
    """test for CalculateDowntimeTests"""
    def setUp(self):
        # Make some Events and fudge the totalTime
        self.e1 = Event("1")
        self.e1.totalTime = datetime.timedelta(minutes=1)
        self.e2 = Event("2")
        self.e2.totalTime = datetime.timedelta(minutes=1)
        self.e3 = Event("3")
        self.e3.totalTime = datetime.timedelta(minutes=1)

    def testEventsOverlapIsZeroDowntime(self):
        """Events with overlapping start and end times should have no downtime between them"""
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 0), self.e1))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 1), self.e2))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 2), self.e3))
        downtime = s.calculateDowntime()
        self.assertEqual(downtime, datetime.timedelta(seconds=0))

    def testEventsAtSameTimeIsZeroDowntime(self):
        """Events that start at the same time should have no downtime between them"""
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1), self.e1))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1), self.e2))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1), self.e3))
        downtime = s.calculateDowntime()
        self.assertEqual(downtime, datetime.timedelta(seconds=0))

    def testEventsOneMinuteApartIsTwo(self):
        """Three Events one minute apart should have 2 minutes downtime"""
        s = Schedule()
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 0), self.e1))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 2), self.e2))
        s.arrangement.append((datetime.datetime(2014, 1, 1, 1, 4), self.e3))
        downtime = s.calculateDowntime()
        self.assertEqual(downtime, datetime.timedelta(minutes=2))

class CalculateFitnessTests(unittest.TestCase):
    """tests for CalculateFitnessTests"""
    
    def testSanity(self):
        """A a Schedule with a single Event within the time parameters is feasible with a fitness of 0"""
        event = Event("1")
        event.totalTime = datetime.timedelta(minutes=1)
        s = Schedule([(datetime.datetime(2014, 1, 1, 10), event)])
        startDateTime = datetime.datetime(2014, 1, 1, 9)
        endDateTime = datetime.datetime(2014, 1, 1, 21)
        lunchStartTime = datetime.datetime(2014, 1, 1, 12)
        lunchEndTime = datetime.datetime(2014, 1, 1, 13)
        dinnerStartTime = datetime.datetime(2014, 1, 1, 17)
        dinnerEndTime = datetime.datetime(2014, 1, 1, 18)
        dayEndTime = datetime.datetime(2014, 1, 1, 21)
        nextDayStartTime = datetime.datetime(2014, 1, 2, 9)
        s.calculateFitness(startDateTime, endDateTime, lunchStartTime, lunchEndTime, dinnerStartTime, dinnerEndTime, dayEndTime, nextDayStartTime)
        self.assertTrue(s.feasible)
        self.assertEqual(s.fitness, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly morre detailed results
