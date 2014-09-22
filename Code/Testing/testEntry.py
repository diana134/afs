"""Unit tests for entry.py"""

import sys
sys.path.insert(0, '../')
import unittest
# import sqlite3
from PyQt4.QtSql import QSqlQuery

from entry import Entry
from databaseInteraction import DatabaseInteraction

class EntryDatabaseTests(unittest.TestCase):
    """test database related functions in Entry"""
    def setUp(self):
        self.db = DatabaseInteraction(test=True)
        # Start fresh
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM entries WHERE title='Foo Bar'")
        self.db.conn.commit()

    def testAddToDB(self):
        """test that a correctly formatted Entry can be added to the database properly"""
        e = Entry(0, 0, 'Piano', 2, 42, 'ABC', 'Foo Bar', '0:42', 'Foo Bar', 'Foo Bar', 3, 4, 5, 'Foo Bar', 'Foo Bar', 'Foo Baritone', 'Foo Bar')
        e.addToDB(self.db)
        # self.conn.commit()
        #query db
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT participant_id, teacher_id, discipline, level, class_number, class_name, title, performance_time, style, composer, opus, no, movement, arranger, artist, instrument, author FROM entries WHERE title='Foo Bar'")
        #check info is same
        self.assertTrue(query.next())
        participantID = query.value(0).toString()
        teacherID = query.value(1).toString()
        discipline = query.value(2).toString()
        level = query.value(3).toString()
        classNumber = query.value(4).toString()
        className = query.value(5).toString()
        title = query.value(6).toString()
        performanceTime = query.value(7).toString()
        style = query.value(8).toString()
        composer = query.value(9).toString()
        opus = query.value(10).toString()
        no = query.value(11).toString()
        movement = query.value(12).toString()
        arranger = query.value(13).toString()
        artist = query.value(14).toString()
        instrument = query.value(15).toString()
        author = query.value(16).toString()
        ee = Entry(participantID, teacherID, discipline, level, classNumber, className, title, performanceTime, style, composer, opus, no, movement, arranger, artist, instrument, author)
        isMatch = e.isEqualTo(ee)
        self.assertTrue(isMatch)

    def tearDown(self):
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM entries WHERE title='Foo Bar'")
        self.db.conn.commit()

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
