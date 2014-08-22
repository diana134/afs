import sys
sys.path.insert(0, '../')
import unittest
import sqlite3

from entry import *

class EntryDatabaseTests(unittest.TestCase):
    """test database related functions in Entry"""
    def setUp(self):
        self.conn = sqlite3.connect('../../Database/AFS')

    def testAddToDB(self):
        """test that a correctly formatted Entry can be added to the database properly"""
        e = Entry('0', '0', '0', '123', 'abc', 'Foo Bar', '1:00')
        e.addToDB(self.conn)
        self.conn.commit()
        #query db
        cursor = self.conn.execute("SELECT * FROM entries WHERE title='Foo Bar'")
        #check info is same
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        participantID = row[1]
        teacherID = row[2]
        level = row[3]
        classNumber = row[4]
        className = row[5]
        title = row[6]
        performanceTime = row[7]
        ee = Entry(participantID, teacherID, level, classNumber, className, title, performanceTime)
        isMatch = e.isEqualTo(ee)
        self.assertTrue(isMatch)

    def tearDown(self):
        self.conn.execute("DELETE FROM entries WHERE title='Foo Bar'")
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results