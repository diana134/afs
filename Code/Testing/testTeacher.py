"""Unit tests for teacher.py"""

import sys
sys.path.insert(0, '../')
import unittest
# import sqlite3
from PyQt4.QtSql import QSqlQuery

from teacher import Teacher
from databaseInteraction import DatabaseInteraction

class TeacherTests(unittest.TestCase):
    """tests non-databse functions in Teacher"""
    def setUp(self):
        self.t = Teacher('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com')

    def testIsEqualToSame(self):
        """test that two identical Teachers are the same"""
        tt = Teacher('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com')
        isMatch = self.t.isEqualTo(tt)
        self.assertTrue(isMatch)

    def testIsEqualToNone(self):
        """test that None in optional fields still matches"""
        tt = Teacher('Foo', 'Bar', None, None, None, None, None, 'foobar@testmail.com')
        isMatch = self.t.isEqualTo(tt)
        self.assertTrue(isMatch)

    def testIsEqualToBlank(self):
        """test that blanks in optional fields still match"""
        tt = Teacher('Foo', 'Bar', '', '', '', '', '', 'foobar@testmail.com')
        isMatch = self.t.isEqualTo(tt)
        self.assertTrue(isMatch)

    def testIsEqualToMissingFields(self):
        """test that missing required fields causes Teacher not to match"""
        tt = Teacher('', '', '', '', '', '', '', '')
        isMatch = self.t.isEqualTo(tt)
        self.assertFalse(isMatch)
        tt = Teacher(None, None, None, None, None, None, None, None)
        isMatch = self.t.isEqualTo(tt)
        self.assertFalse(isMatch)

class TeacherDatabaseTests(unittest.TestCase):
    """test database related functions in Teacher"""
    def setUp(self):
        self.db = DatabaseInteraction(test=True)
        # Start fresh
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        self.db.conn.commit()

    def testAddToDB(self):
        """test that a correctly formatted Teacher can be added to the database properly"""
        t = Teacher('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', '1234567890', '1234567890', 'foobar@testmail.com')
        t.addToDB(self.db)
        #query db
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT first_name, last_name, address, city, postal_code, daytime_phone, evening_phone, email FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        #check info is same
        self.assertTrue(query.next())
        first = query.value(0).toString()
        last = query.value(1).toString()
        address = query.value(2).toString()
        city = query.value(3).toString()
        postal = query.value(4).toString()
        daytimePhone = query.value(5).toString()
        eveningPhone = query.value(6).toString()
        email = query.value(7).toString()
        tt = Teacher(first, last, address, city, postal, daytimePhone, eveningPhone, email)
        isMatch = t.isEqualTo(tt)
        self.assertTrue(isMatch)

    def tearDown(self):
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        self.db.conn.commit()
        self.db.close()

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
    