"""Handles all interactions with the database"""

import sys
import os
# import sqlite3
from PyQt4.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

from participant import SoloParticipant, GroupParticipant
from teacher import Teacher
from entry import Entry

CONFIG_DATABASE_PATH = "../Database/"
CONFIG_TEST_DATABASE_PATH = "../../Database/"
CONFIG_DATABASE_NAME = "AFS"

class DatabaseInteraction(object):
    """Handles all interactions with the database"""
    def __init__(self, test=False):
        # filename = os.path.join(CONFIG_DATABASE_PATH, CONFIG_DATABASE_NAME)
        # self.conn = sqlite3.connect(filename)
        # # Check that the db opened successfully, close program if it didn't
        # # TODO: handle this better?
        # if self.conn is None:
        #     print "Failed to open database " + filename
        #     sys.exit(1)
        if test:
            filename = os.path.join(CONFIG_TEST_DATABASE_PATH, CONFIG_DATABASE_NAME)
        else:
            filename = os.path.join(CONFIG_DATABASE_PATH, CONFIG_DATABASE_NAME)
        self.conn = QSqlDatabase.addDatabase("QSQLITE")
        self.conn.setDatabaseName(filename)
        result = self.conn.open()
        # Check that the db opened successfully, close program if it didn't
        # TODO: handle this better?
        if result == False:
            print "Failed to open database " + filename + \
                " with error: " + self.conn.lastError().text()
            sys.exit(1)
        
        # SoloParticipant
        self.soloParticipantModel = QSqlTableModel(db=self.conn)
        self.soloParticipantModel.setTable("soloparticipants")
        self.soloParticipantModel.select()

        # GroupParticipant
        self.groupParticipantModel = QSqlTableModel(db=self.conn)
        self.groupParticipantModel.setTable("groupparticipants")
        self.groupParticipantModel.select()

        # Teacher
        self.teacherModel = QSqlTableModel(db=self.conn)
        self.teacherModel.setTable("teachers")
        self.teacherModel.select()

    def close(self):
        """Clean everything up and close the connection"""
        connName = self.conn.connectionName()
        self.conn.close()
        self.conn = QSqlDatabase()
        self.conn.removeDatabase(connName)

    def addSoloParticipant(self, values):
        """Adds a new SoloParticipant record to the db"""
        # try:
        #     query = "INSERT INTO soloparticipants (first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        #     self.conn.execute(query, values)
        #     self.conn.commit()
        #     return ""
        # except Exception, e:
        #     # TODO: log this instead of printing to console
        #     print "addSoloParticipant FAILED\n\tquery: {0}\n\tvalues: {1}\n\terror: {2}".format(query, values, e)
        #     return e
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO soloparticipants \
                (first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
            for value in values:
                query.addBindValue(value)
            query.exec_()
            self.soloParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addSoloParticipant FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query, values, e)
            return e

    def addGroupParticipant(self, values):
        """Adds a new GroupParticipant record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO groupparticipants \
                (group_name, group_size, school_grade, average_age, participants) \
                VALUES (?, ?, ?, ?, ?)")
            for value in values:
                query.addBindValue(value)
            query.exec_()
            self.groupParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addGroupParticipant FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query.lastQuery(), values, e)
            return e

    def addTeacher(self, values):
        """Adds a new Teacher record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO teachers \
                (first_name, last_name, address, city, postal_code, daytime_phone, evening_phone, email) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
            for value in values:
                query.addBindValue(value)
            query.exec_()
            self.teacherModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addTeacher FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query.lastQuery(), values, e)
            return e

    def addEntry(self, values):
        """Adds a new Entry record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO entries \
                (participant_id, teacher_id, discipline, level, class_number, class_name, title, performance_time, style, composer, opus, no, movement, arranger, artist, instrument, author) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
            for value in values:
                query.addBindValue(value)
            query.exec_()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addEntry FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query.lastQuery(), values, e)
            return e

    #####

    def getParticipantFromId(self, participantId):
        """Retrieve the appropriate Participant from the given id"""
        try:
            query = QSqlQuery(self.conn)
            if participantId[0] == 's':
                query.prepare("SELECT first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth \
                    FROM soloparticipants WHERE id=:id")
            else:
                query.prepare("SELECT group_name, group_size, school_grade, average_age, participants \
                    FROM groupparticipants WHERE id=:id")
            numericId = participantId[1:]
            query.bindValue(":id", numericId)
            query.exec_()
            # Now turn it into the appropriate object
            query.next()
            retrievedParticipant = None
            if participantId[0] == 's':
                first = query.value(0).toString()
                last = query.value(1).toString()
                address = query.value(2).toString()
                town = query.value(3).toString()
                postal = query.value(4).toString()
                home = query.value(5).toString()
                cell = query.value(6).toString()
                email = query.value(7).toString()
                dob = query.value(8).toString()
                retrievedParticipant = SoloParticipant(first, last, address, town, postal, home, cell, email, dob)
            else:
                groupName = query.value(0).toString()
                groupSize = query.value(1).toString()
                schoolGrade = query.value(2).toString()
                averageAge = query.value(3).toString()
                participants = query.value(4).toString()
                retrievedParticipant = GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants)
            return retrievedParticipant
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getParticipantFromId FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query.lastQuery(), numericId, e)

    def getLastSoloParticipantId(self):
        """Get the id of the most recently added SoloParticipant"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT id from soloparticipants WHERE id=(SELECT MAX(id) FROM soloparticipants)")
            query.next()
            participantId = query.value(0).toString()
            return "s" + participantId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastSoloParticipantId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    def getLastGroupParticipantId(self):
        """Get the id of the most recently added GroupParticipant"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT id from groupparticipants WHERE id=(SELECT MAX(id) FROM groupparticipants)")
            query.next()
            participantId = query.value(0).toString()
            return "g" + participantId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastSoloParticipantId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    def getTeacherFromId(self, teacherId):
        """Retrieve the appropriate Teacher from the given id"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT first_name, last_name, address, city, postal_code, daytime_phone, evening_phone, email \
                    FROM teachers WHERE id=:id")
            numericId = teacherId
            query.bindValue(":id", numericId)
            query.exec_()
            # Now turn it into the appropriate object
            query.next()
            first = query.value(0).toString()
            last = query.value(1).toString()
            address = query.value(2).toString()
            city = query.value(3).toString()
            postal = query.value(4).toString()
            daytimePhone = query.value(5).toString()
            eveningPhone = query.value(6).toString()
            email = query.value(7).toString()
            retrievedTeacher = Teacher(first, last, address, city, postal, daytimePhone, eveningPhone, email)
            return retrievedTeacher
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getTeacherFromId FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query.lastQuery(), numericId, e)

    def getLastTeacherId(self):
        """Get the id of the most recently added Teacher"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT id from teachers WHERE id=(SELECT MAX(id) FROM teachers)")
            query.next()
            teacherId = query.value(0).toString()
            return teacherId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastTeacherIdFAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    #####

    def getAllEntries(self):
        """Retrieve all the Entries and return them in a list"""
        entryList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT participant_id, teacher_id, discipline, level, class_number, \
                class_name, title, performance_time, style, composer, opus, no, movement, arranger, \
                artist, instrument, author FROM entries")
            query.exec_()
            while query.next() == True:
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
                entryList.append(ee)
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastTeacherIdFAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
        return entryList
        