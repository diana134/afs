"""Unit tests for participant.py"""

import sys
sys.path.insert(0, '../')
import unittest

from participant import SoloParticipant, GroupParticipant

class ParticipantTests(unittest.TestCase):
    """tests non-databse functions in Participant"""
    def setUp(self):
        self.sp = SoloParticipant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com', '1900-01-01')
        self.gp = GroupParticipant('Foo', 1, 1, 1, 'Foo Bar')

    def testIsEqualToSame(self):
        """test that two identical Participants are the same"""
        spp = SoloParticipant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com', '1900-01-01')
        isMatch = self.sp.isEqualTo(spp)
        self.assertTrue(isMatch)
        gpp = GroupParticipant('Foo', 1, 1, 1, 'Foo Bar')
        isMatch = self.gp.isEqualTo(gpp)
        self.assertTrue(isMatch)

    def testIsEqualToNone(self):
        """test that None in optional fields still matches"""
        spp = SoloParticipant('Foo', 'Bar', None, None, None, None, None, None, '1900-01-01')
        isMatch = self.sp.isEqualTo(spp)
        self.assertTrue(isMatch)
        gpp = GroupParticipant('Foo', None, None, None, None)
        isMatch = self.gp.isEqualTo(gpp)
        self.assertTrue(isMatch)

    def testIsEqualToBlank(self):
        """test that blanks in optional fields still match"""
        spp = SoloParticipant('Foo', 'Bar', '', '', '', '', '', '', '1900-01-01')
        isMatch = self.sp.isEqualTo(spp)
        self.assertTrue(isMatch)
        gpp = GroupParticipant('Foo', '', '', '', '')
        isMatch = self.gp.isEqualTo(gpp)
        self.assertTrue(isMatch)

    def testIsEqualToMissingFields(self):
        """test that missing required fields causes Participant not to match"""
        spp = SoloParticipant('', '', '', '', '', '', '', '', '')
        isMatch = self.sp.isEqualTo(spp)
        self.assertFalse(isMatch)
        spp = SoloParticipant(None, None, None, None, None, None, None, None, None)
        isMatch = self.sp.isEqualTo(spp)
        self.assertFalse(isMatch)
        gpp = GroupParticipant('', '', '', '', '')
        isMatch = self.gp.isEqualTo(gpp)
        self.assertFalse(isMatch)
        gpp = GroupParticipant(None, None, None, None, None)
        isMatch = self.gp.isEqualTo(gpp)
        self.assertFalse(isMatch)

# GUI testing is overly fiddly and time consuming :/
# class AddSoloParticipantDialogTests(unittest.TestCase):
    
#     def setUp(self):
#         # self.app = QApplication(sys.argv)
#         self.conn = sqlite3.connect('../../Database/AFS')
#         self.form = MainWindow(True, self.conn)
#         self.p = Participant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', 1234567890, 1234567890, 'foobar@testmail.com', '1901-01-01')

#     @classmethod
#     def setUpClass(cls):
#         cls._app = QApplication([])

#     @classmethod
#     def tearDownClass(cls):
#         del cls._app

#     def tearDown(self):
#         self.conn.execute("DELETE FROM participants WHERE first_name='Foo' AND last_name='Bar'")
#         self.conn.commit()
#         self.conn.close()
#         # del self.app

#     def testAddNewParticipantCorrect(self):
#         """tests adding a correctly formatted new Participant from the GUI"""
#         # Clear and then type test data into the participant form
#         self.form.ui.firstNameLineEdit.clear()
#         QTest.keyClicks(self.form.ui.firstNameLineEdit, "Foo")
#         self.form.ui.lastNameLineEdit.clear()
#         QTest.keyClicks(self.form.ui.lastNameLineEdit, "Bar")
#         self.form.ui.addressLineEdit.clear()
#         QTest.keyClicks(self.form.ui.addressLineEdit, "123 Anywhere St.")
#         self.form.ui.cityLineEdit.clear()
#         QTest.keyClicks(self.form.ui.cityLineEdit, "Sometown")
#         self.form.ui.postalCodeLineEdit.clear()
#         QTest.keyClicks(self.form.ui.postalCodeLineEdit, "1Q2W3E")
#         self.form.ui.homePhoneLineEdit.clear()
#         QTest.keyClicks(self.form.ui.homePhoneLineEdit, "1234567890")
#         self.form.ui.cellPhoneLineEdit.clear()
#         QTest.keyClicks(self.form.ui.cellPhoneLineEdit, "1234567890")
#         self.form.ui.emailLineEdit.clear()
#         QTest.keyClicks(self.form.ui.emailLineEdit, "foobar@testmail.com")
#         self.form.ui.dateOfBirthDateEdit.setDate(QDate(1901,1,1))
#         self.assertEqual(self.form.ui.dateOfBirthDateEdit.date(), QDate(1901,1,1))

#         # Push Add Participant button with the left mouse button
#         QTest.mouseClick(self.form.ui.addParticipantBtn, Qt.LeftButton)
#         # Query db
#         cursor = self.conn.execute("SELECT first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth FROM participants WHERE first_name='Foo' AND last_name='Bar'")
#         # Check info is same
#         row = cursor.fetchone()
#         self.assertIsNotNone(row)
#         first = row[0]
#         last = row[1]
#         address = row[2]
#         town = row[3]
#         postal = row[4]
#         home = row[5]
#         cell = row[6]
#         email = row[7]
#         dob = row[8]
#         pp = Participant(first, last, address, town, postal, home, cell, email, dob)
#         isMatch = self.p.isEqualTo(pp)
#         self.assertTrue(isMatch)

#     def testAddNewParticipantIncorrect(self):
#         """tests that trying to add a Participant missing a required field fails"""
#       # Clear and then type test data into the participant form
#         self.form.ui.firstNameLineEdit.clear()
#         QTest.keyClicks(self.form.ui.firstNameLineEdit, "Foo")
#         self.form.ui.lastNameLineEdit.clear()
#         QTest.keyClicks(self.form.ui.lastNameLineEdit, "Bar")
#         self.form.ui.addressLineEdit.clear()
#         QTest.keyClicks(self.form.ui.addressLineEdit, "123 Anywhere St.")
#         self.form.ui.cityLineEdit.clear()
#         QTest.keyClicks(self.form.ui.cityLineEdit, "Sometown")
#         self.form.ui.postalCodeLineEdit.clear()
#         QTest.keyClicks(self.form.ui.postalCodeLineEdit, "1Q2W3E")
#         self.form.ui.homePhoneLineEdit.clear()
#         QTest.keyClicks(self.form.ui.homePhoneLineEdit, "1234567890")
#         self.form.ui.cellPhoneLineEdit.clear()
#         QTest.keyClicks(self.form.ui.cellPhoneLineEdit, "1234567890")
#         self.form.ui.emailLineEdit.clear()
#         QTest.keyClicks(self.form.ui.emailLineEdit, "foobar@testmail.com")
#         # Purposely leave out dob

#         # Push Add Participant button with the left mouse button
#         QTest.mouseClick(self.form.ui.addParticipantBtn, Qt.LeftButton)
#         # Query db
#         cursor = self.conn.execute("SELECT first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth FROM participants WHERE first_name='Foo' AND last_name='Bar'")
#         # Check that nothing was inserted
#         row = cursor.fetchone()
#         self.assertIsNone(row)
        

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
