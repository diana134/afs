import sys
sys.path.insert(0, '../')
from participant import Participant
import unittest
import sqlite3
# from atest import DatePattern
# import datetime

# class FooTests(unittest.TestCase):

#     # def testFoo(self):
#     #     self.failUnless(False)

#     # An example test for atest.py
# 	def testMatches(self):
# 	    p = DatePattern(2004, 9, 28)
# 	    d = datetime.date(2004, 9, 28)
# 	    self.failUnless(p.matches(d))

class ParticipantTests(unittest.TestCase):
	"""tests non-databse functions in Participant"""
	def setUp(self):
		self.p = Participant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com', '1900-01-01')

	def testIsEqualToSame(self):
		pp = Participant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com', '1900-01-01')
		isMatch = self.p.isEqualTo(pp)
		self.assertTrue(isMatch)

	def testIsEqualToNone(self):
		pp = Participant('Foo', 'Bar', None, None, None, None, None, None, '1900-01-01')
		isMatch = self.p.isEqualTo(pp)
		self.assertTrue(isMatch)

	def testIsEqualToBlank(self):
		pp = Participant('Foo', 'Bar', '', '', '', '', '', '', '1900-01-01')
		isMatch = self.p.isEqualTo(pp)
		self.assertTrue(isMatch)

	def testIsEqualToMissingFields(self):
		pp = Participant('', '', '', '', '', '', '', '', '')
		isMatch = self.p.isEqualTo(pp)
		self.assertFalse(isMatch)
		pp = Participant(None, None, None, None, None, None, None, None, None)
		isMatch = self.p.isEqualTo(pp)
		self.assertFalse(isMatch)

class ParticipantDatabaseTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect('../../Database/AFS')

	def testAddToDB(self):
		p = Participant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', '1234567890', '1234567890', 'foobar@testmail.com', '1900-01-01')
		p.addToDB(self.conn)
		self.conn.commit()
		#query db
		cursor = self.conn.execute("SELECT first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth FROM participants WHERE first_name='Foo' AND last_name='Bar'")
		#check info is same
		row = cursor.fetchone()
		self.assertIsNotNone(row)
		first = row[0]
		last = row[1]
		address = row[2]
		town = row[3]
		postal = row[4]
		home = row[5]
		cell = row[6]
		email = row[7]
		dob = row[8]
		pp = Participant(first, last, address, town, postal, home, cell, email, dob)
		isMatch = p.isEqualTo(pp)
		self.assertTrue(isMatch)

	def tearDown(self):
		self.conn.execute("DELETE FROM participants WHERE first_name='Foo' AND last_name='Bar'")
		self.conn.commit()
		self.conn.close()


def main():
	unittest.main()

if __name__ == '__main__':
	main()