"""Unit tests for databaseInteraction.py"""

import sys
sys.path.insert(0, '../')
import unittest
from PyQt4.QtSql import QSqlQuery

from databaseInteraction import DatabaseInteraction
from participant import SoloParticipant, GroupParticipant
from teacher import Teacher
from entry import Entry

class ParticipantDatabaseTests(unittest.TestCase):
    """test database interactions for Participants"""
    def setUp(self):
        self.db = DatabaseInteraction(test=True)
        # Start fresh
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM soloparticipants WHERE first_name='Foo' AND last_name='Bar'")
        query.exec_("DELETE FROM groupparticipants WHERE group_name='Foo'")
        self.db.conn.commit()

    def testSoloParticipantAddToDB(self):
        """test that a correctly formatted SoloParticipant can be added to the database properly"""
        sp = SoloParticipant('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', '1234567890', '1234567890', 'foobar@testmail.com', '1900-01-01')
        sp.addToDB(self.db)
        #query db
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT first_name, last_name, address, town, postal_code, home_phone, \
            cell_phone, email, date_of_birth \
            FROM soloparticipants WHERE first_name='Foo' AND last_name='Bar'")
        #check info is same
        self.assertTrue(query.next())
        first = query.value(0).toString()
        last = query.value(1).toString()
        address = query.value(2).toString()
        town = query.value(3).toString()
        postal = query.value(4).toString()
        home = query.value(5).toString()
        cell = query.value(6).toString()
        email = query.value(7).toString()
        dob = query.value(8).toString()
        spp = SoloParticipant(first, last, address, town, postal, home, cell, email, dob)
        isMatch = spp.isEqualTo(sp)
        self.assertTrue(isMatch)

    def testGroupParticipantAddToDB(self):
        """test that a correctly formatted GroupParticipant can be added to the database properly"""
        gp = GroupParticipant('Foo', '2', '2', '8', 'Foo Bar, Foo Bar2')
        gp.addToDB(self.db)
        #query db
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT group_name, group_size, school_grade, average_age, participants \
            FROM groupparticipants WHERE group_name='Foo'")
        #check info is same
        self.assertTrue(query.next())
        groupName = query.value(0).toString()
        groupSize = query.value(1).toString()
        schoolGrade = query.value(2).toString()
        averageAge = query.value(3).toString()
        participants = query.value(4).toString()
        gpp = GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants)
        isMatch = gpp.isEqualTo(gp)
        self.assertTrue(isMatch)

    def testGetParticipantFromId(self):
        """test that the correct Participant can be retrieved based on id"""
        # Create some Participants
        sp = SoloParticipant(first="Foo", last="Bar")
        gp = GroupParticipant(groupName="Foo")
        # Add them to the db
        sp.addToDB(self.db)
        gp.addToDB(self.db)
        # Get the id of each
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT id FROM soloparticipants WHERE first_name='Foo'")
        self.assertTrue(query.next())
        spId = query.value(0).toString()
        query.exec_("SELECT id FROM groupparticipants WHERE group_name='Foo'")
        self.assertTrue(query.next())
        gpId = query.value(0).toString()
        # Get the Participants back based on id
        spId = "s" + spId
        spp = self.db.getParticipantFromId(spId)
        gpId = "g" + gpId
        gpp = self.db.getParticipantFromId(gpId)
        # Check that they match
        isMatch = spp.isEqualTo(sp)
        self.assertTrue(isMatch)
        isMatch = gpp.isEqualTo(gp)
        self.assertTrue(isMatch)

    def testGetLastSoloParticipantId(self):
        """test that the Solo Participant with the max id is the last one we added"""
        # Create some SoloParticipants
        sp1 = SoloParticipant(first="Foo", last="Bar", address="1")
        sp2 = SoloParticipant(first="Foo", last="Bar", address="2")
        sp3 = SoloParticipant(first="Foo", last="Bar", address="3")
        # Add them to the db
        sp1.addToDB(self.db)
        sp2.addToDB(self.db)
        sp3.addToDB(self.db)
        # Get the max id
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT MAX(id) FROM soloparticipants")
        self.assertTrue(query.next())
        maxId = query.value(0).toString()
        # Get id of most recently added SoloParticipant
        query.exec_("SELECT id FROM soloparticipants \
            WHERE first_name='Foo' and last_name='Bar' and address='3'")
        self.assertTrue(query.next())
        newId = query.value(0).toString()
        # Check that they match
        self.assertTrue(maxId == newId)

    def testGetLastGroupParticipantId(self):
        """test that the Group Participant with the max id is the last one we added"""
        # Create some SoloParticipants
        gp1 = GroupParticipant(groupName="Foo", groupSize="1")
        gp2 = GroupParticipant(groupName="Foo", groupSize="2")
        gp3 = GroupParticipant(groupName="Foo", groupSize="3")
        # Add them to the db
        gp1.addToDB(self.db)
        gp2.addToDB(self.db)
        gp3.addToDB(self.db)
        # Get the max id
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT MAX(id) FROM groupparticipants")
        self.assertTrue(query.next())
        maxId = query.value(0).toString()
        # Get id of most recently added GroupParticipant
        query.exec_("SELECT id FROM groupparticipants \
            WHERE group_name='Foo' and group_size='3'")
        self.assertTrue(query.next())
        newId = query.value(0).toString()
        # Check that they match
        self.assertTrue(maxId == newId)

    def tearDown(self):
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM soloparticipants WHERE first_name='Foo' AND last_name='Bar'")
        query.exec_("DELETE FROM groupparticipants WHERE group_name='Foo'")
        self.db.conn.commit()
        self.db.close()

class TeacherDatabaseTests(unittest.TestCase):
    """test database interactions for Teachers"""
    def setUp(self):
        self.db = DatabaseInteraction(test=True)
        # Start fresh
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        self.db.conn.commit()

    def testTeacherAddToDB(self):
        """test that a correctly formatted Teacher can be added to the database properly"""
        t = Teacher('Foo', 'Bar', '123 Anywhere St.', 'Sometown', '1Q2W3E', '1234567890', '1234567890', 'foobar@testmail.com')
        t.addToDB(self.db)
        #query db
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT first_name, last_name, address, city, postal_code, daytime_phone, \
            evening_phone, email FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
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

    def testGetTeacherFromId(self):
        """test that the correct Teacher can be retrieved based on id"""
        # Create a Teacher
        t = Teacher(first="Foo", last="Bar")
        # Add it to the db
        t.addToDB(self.db)
        # Get the id
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT id FROM teachers WHERE first_name='Foo'")
        self.assertTrue(query.next())
        tId = query.value(0).toString()
        # Get the Teacher back based on id
        tt = self.db.getTeacherFromId(tId)
        # Check that they match
        isMatch = tt.isEqualTo(t)
        self.assertTrue(isMatch)

    def testGetLastTeacherId(self):
        """test that the Teacher with the max id is the last one we added"""
        # Create some Teachers
        t1 = Teacher(first="Foo", last="Bar", email="1")
        t2 = Teacher(first="Foo", last="Bar", email="2")
        t3 = Teacher(first="Foo", last="Bar", email="3")
        # Add them to the db
        t1.addToDB(self.db)
        t2.addToDB(self.db)
        t3.addToDB(self.db)
        # Get the max id
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT MAX(id) FROM teachers")
        self.assertTrue(query.next())
        maxId = query.value(0).toString()
        # Get id of most recently added Teacher
        query.exec_("SELECT id FROM teachers \
            WHERE first_name='Foo' and last_name='Bar' and email='3'")
        self.assertTrue(query.next())
        newId = query.value(0).toString()
        # Check that they match
        self.assertTrue(maxId == newId)

    def tearDown(self):
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM teachers WHERE first_name='Foo' AND last_name='Bar'")
        self.db.conn.commit()
        self.db.close()

class EntryDatabaseTests(unittest.TestCase):
    """test database interactions for Entries"""
    def setUp(self):
        self.db = DatabaseInteraction(test=True)
        # Start fresh
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM entries WHERE title='Foo Bar'")
        self.db.conn.commit()

    def testEntryAddToDB(self):
        """test that a correctly formatted Entry can be added to the database properly"""
        e = Entry(0, 0, 'Piano', 2, 42, 'ABC', 'Foo Bar', '0:42', 'Foo Bar', 'Foo Bar', 3, 4, 5, 'Foo Bar', 'Foo Bar', 'Foo Baritone', 'Foo Bar')
        e.addToDB(self.db)
        #query db
        query = QSqlQuery(self.db.conn)
        query.exec_("SELECT participant_id, teacher_id, discipline, level, class_number, \
            class_name, title, performance_time, style, composer, opus, no, movement, arranger, \
            artist, instrument, author FROM entries WHERE title='Foo Bar'")
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

    def testGetAllEntries(self):
        """test that all added Entries can be retrieved in a list"""
        # Make some Entries
        e1 = Entry(0, 0, 'Piano', 2, 42, 'ABC', 'Foo Bar', '0:42', 'Foo Bar', 'Foo Bar', 3, 4, 5, 'Foo Bar', 'Foo Bar', 'Foo Baritone', 'Foo Bar')
        e2 = Entry(participantID="2", teacherID="2", classNumber="2", className="", title="Foo Bar")
        e3 = Entry(participantID="3", teacherID="3", classNumber="3", className="", title="Foo Bar")
        # Add them to the db
        e1.addToDB(self.db)
        e2.addToDB(self.db)
        e3.addToDB(self.db)
        # Retrieve the list
        entryList = self.db.getAllEntries()
        # Make sure it has the right number of elements
        self.assertTrue(len(entryList) == 3)
        # Make sure each of the Entries are in the list
        for entry in entryList:
            if not entry.isEqualTo(e1) and not entry.isEqualTo(e2) and not entry.isEqualTo(e3):
                self.assertTrue(False)

    def tearDown(self):
        query = QSqlQuery(self.db.conn)
        query.exec_("DELETE FROM entries WHERE title='Foo Bar'")
        self.db.conn.commit()
        self.db.close()

if __name__ == '__main__':
    unittest.main(verbosity=2) # for slightly more detailed results
