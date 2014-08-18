import sys
sys.path.insert(0, '../')
import unittest
import sqlite3

from teacher import Teacher

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
        self.conn = sqlite3.connect('../../Database/AFS')

    def testAddToDB(self):
        """test that a correctly formatted Teacher can be added to the database properly"""
        t = Teacher('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', '1234567890', '1234567890', 'foobar@testmail.com')
        t.addToDB(self.conn)
        self.conn.commit()
        #query db
        cursor = self.conn.execute("SELECT first_name, last_name, address, city, postal_code, daytime_phone, evening_phone, email FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        #check info is same
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        first = row[0]
        last = row[1]
        address = row[2]
        city = row[3]
        postal = row[4]
        daytimePhone = row[5]
        eveningPhone = row[6]
        email = row[7]
        tt = Teacher(first, last, address, city, postal, daytimePhone, eveningPhone, email)
        isMatch = t.isEqualTo(tt)
        self.assertTrue(isMatch)

    def tearDown(self):
        self.conn.execute("DELETE FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results