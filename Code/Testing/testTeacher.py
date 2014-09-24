"""Unit tests for teacher.py"""

import sys
sys.path.insert(0, '../')
import unittest

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

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
    