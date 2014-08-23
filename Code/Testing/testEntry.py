import sys
sys.path.insert(0, '../')
import unittest
import sqlite3

from entry import *

class EntryDatabaseTests(unittest.TestCase):
    """test database related functions in Entry"""
    def setUp(self):
        self.conn = sqlite3.connect('../../Database/AFS')
        # Start fresh
        self.conn.execute("DELETE FROM entries WHERE title='Foo Bar'")
        self.conn.commit()

    def testAddToDB(self):
        """test that a correctly formatted Entry can be added to the database properly"""
        e = Entry(6, 1, 'Piano', 2, 42, 'ABC', 'Foo Bar', '0:42', 'Foo Bar', 'Foo Bar', 3, 4, 5, 'Foo Bar', 'Foo Bar', 'Foo Baritone', 'Foo Bar')
        e.addToDB(self.conn)
        self.conn.commit()
        #query db
        cursor = self.conn.execute("SELECT participant_id, teacher_id, discipline, level, class_number, class_name, title, performance_time, style, composer, opus, no, movement, arranger, artist, instrument, author FROM entries WHERE title='Foo Bar'")
        #check info is same
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        participantID = row[0]
        teacherID = row[1]
        discipline = row[2]
        level = row[3]
        classNumber = row[4]
        className = row[5]
        title = row[6]
        performanceTime = row[7]
        style = row[8]
        composer = row[9]
        opus = row[10]
        no = row[11]
        movement = row[12]
        arranger = row[13]
        artist = row[14]
        instrument = row[15]
        author = row[16]
        ee = Entry(participantID, teacherID, discipline, level, classNumber, className, title, performanceTime, style, composer, opus, no, movement, arranger, artist, instrument, author)
        isMatch = e.isEqualTo(ee)
        self.assertTrue(isMatch)

    def tearDown(self):
        self.conn.execute("DELETE FROM entries WHERE title='Foo Bar'")
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results