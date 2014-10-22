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
        
        global dbInteractionInstance 
        dbInteractionInstance = None

    def addSoloParticipant(self, sp):
        """Adds a new SoloParticipant record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO soloparticipants \
                (first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth) \
                VALUES (:first, :last, :address, :town, :postal, :home, :cell, :email, :dob)")
            query.bindValue(":first", sp.first)
            query.bindValue(":last", sp.last)
            query.bindValue(":address", sp.address)
            query.bindValue(":town", sp.town)
            query.bindValue(":postal", sp.postal)
            query.bindValue(":home", sp.home)
            query.bindValue(":cell", sp.cell)
            query.bindValue(":email", sp.email)
            query.bindValue(":dob", sp.dob)
            query.exec_()
            self.soloParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addSoloParticipant FAILED\n\tquery: {0}\n\terror: {1}".format(query, e)
            return e

    def addGroupParticipant(self, gp):
        """Adds a new GroupParticipant record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO groupparticipants \
                (group_name, group_size, school_grade, average_age, participants) \
                VALUES (:groupName, :groupSize, :schoolGrade, :averageAge, :participants)")
            query.bindValue(":groupName", gp.groupName)
            query.bindValue(":groupSize", gp.groupSize)
            query.bindValue(":schoolGrade", gp.schoolGrade)
            query.bindValue(":averageAge", gp.averageAge)
            query.bindValue(":participants", gp.participants)
            query.exec_()
            self.groupParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addGroupParticipant FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def addTeacher(self, t):
        """Adds a new Teacher record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO teachers \
                (first_name, last_name, address, city, postal_code, daytime_phone, evening_phone, email) \
                VALUES (:first, :last, :address, :city, :postal, :daytimePhone, :eveningPhone, :email)")
            query.bindValue(":first", t.first)
            query.bindValue(":last", t.last)
            query.bindValue(":address", t.address)
            query.bindValue(":city", t.city)
            query.bindValue(":postal", t.postal)
            query.bindValue(":daytimePhone", t.daytimePhone)
            query.bindValue(":eveningPhone", t.eveningPhone)
            query.bindValue(":email", t.email)
            query.exec_()
            self.teacherModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addTeacher FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def addEntry(self, entry):
        """Adds a new Entry record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO entries \
                (participant_id, teacher_id, discipline, level, class_number, class_name, title, performance_time, style, composer, opus, no, movement, arranger, artist, instrument, author) \
                VALUES (:participantID, :teacherID, :discipline, :level, :classNumber, :className, :title, :performanceTime, :style, :composer, :opus, :no, :movement, :arranger, :artist, :instrument, :author)")
            query.bindValue(":participantID", entry.participantID)
            query.bindValue(":teacherID", entry.teacherID)
            query.bindValue(":discipline", entry.discipline)
            query.bindValue(":level", entry.level)
            query.bindValue(":classNumber", entry.classNumber)
            query.bindValue(":className", entry.className)
            query.bindValue(":title", entry.title)
            query.bindValue(":performanceTime", entry.performanceTime)
            query.bindValue(":style", entry.style)
            query.bindValue(":composer", entry.composer)
            query.bindValue(":opus", entry.opus)
            query.bindValue(":no", entry.no)
            query.bindValue(":movement", entry.movement)
            query.bindValue(":arranger", entry.arranger)
            query.bindValue(":artist", entry.artist)
            query.bindValue(":instrument", entry.instrument)
            query.bindValue(":author", entry.author)
            query.exec_()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addEntry FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
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
                first = str(query.value(0).toString())
                last = str(query.value(1).toString())
                address = str(query.value(2).toString())
                town = str(query.value(3).toString())
                postal = str(query.value(4).toString())
                home = str(query.value(5).toString())
                cell = str(query.value(6).toString())
                email = str(query.value(7).toString())
                dob = str(query.value(8).toString())
                retrievedParticipant = SoloParticipant(first, last, address, town, postal, home, cell, email, dob)
            else:
                groupName = str(query.value(0).toString())
                groupSize = str(query.value(1).toString())
                schoolGrade = str(query.value(2).toString())
                averageAge = str(query.value(3).toString())
                participants = str(query.value(4).toString())
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
            query.exec_("SELECT MAX(id) FROM soloparticipants")
            query.next()
            participantId = str(query.value(0).toString())
            return "s" + participantId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastSoloParticipantId FAILED\n\tquery: {0}\
                \n\terror: {1}".format(query.lastQuery(), e)

    def getLastGroupParticipantId(self):
        """Get the id of the most recently added GroupParticipant"""
        try:
            query = QSqlQuery(self.conn)
            query.exec_("SELECT MAX(id) FROM groupparticipants")
            query.next()
            participantId = str(query.value(0).toString())
            return "g" + participantId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastSoloParticipantId FAILED\n\tquery: {0}\
                \n\terror: {1}".format(query.lastQuery(), e)

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
            first = str(query.value(0).toString())
            last = str(query.value(1).toString())
            address = str(query.value(2).toString())
            city = str(query.value(3).toString())
            postal = str(query.value(4).toString())
            daytimePhone = str(query.value(5).toString())
            eveningPhone = str(query.value(6).toString())
            email = str(query.value(7).toString())
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
            teacherId = str(query.value(0).toString())
            return teacherId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastTeacherId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

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
                participantID = str(query.value(0).toString())
                teacherID = str(query.value(1).toString())
                discipline = str(query.value(2).toString())
                level = str(query.value(3).toString())
                classNumber = str(query.value(4).toString())
                className = str(query.value(5).toString())
                title = str(query.value(6).toString())
                performanceTime = str(query.value(7).toString())
                style = str(query.value(8).toString())
                composer = str(query.value(9).toString())
                opus = str(query.value(10).toString())
                no = str(query.value(11).toString())
                movement = str(query.value(12).toString())
                arranger = str(query.value(13).toString())
                artist = str(query.value(14).toString())
                instrument = str(query.value(15).toString())
                author = str(query.value(16).toString())
                ee = Entry(participantID, teacherID, discipline, level, classNumber, className, title, performanceTime, style, composer, opus, no, movement, arranger, artist, instrument, author)
                entryList.append(ee)
            return entryList
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getAllEntries FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    def getAllEntriesInDiscipline(self, discipline):
        """Returns all the Entries for the given discipline"""
        entryList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT participant_id, teacher_id, discipline, level, class_number, \
                class_name, title, performance_time, style, composer, opus, no, movement, arranger, \
                artist, instrument, author FROM entries WHERE discipline=:discipline")
            query.bindValue(":discipline", discipline)
            query.exec_()
            while query.next() == True:
                participantID = str(query.value(0).toString())
                teacherID = str(query.value(1).toString())
                discipline = str(query.value(2).toString())
                level = str(query.value(3).toString())
                classNumber = str(query.value(4).toString())
                className = str(query.value(5).toString())
                title = str(query.value(6).toString())
                performanceTime = str(query.value(7).toString())
                style = str(query.value(8).toString())
                composer = str(query.value(9).toString())
                opus = str(query.value(10).toString())
                no = str(query.value(11).toString())
                movement = str(query.value(12).toString())
                arranger = str(query.value(13).toString())
                artist = str(query.value(14).toString())
                instrument = str(query.value(15).toString())
                author = str(query.value(16).toString())
                ee = Entry(participantID, teacherID, discipline, level, classNumber, className, title, performanceTime, style, composer, opus, no, movement, arranger, artist, instrument, author)
                entryList.append(ee)
            return entryList
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getAllEntriesInDiscipline FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

# Global variable
dbInteractionInstance = DatabaseInteraction()
