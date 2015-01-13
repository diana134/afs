"""Handles all interactions with the database"""

import sys
import os
# import sqlite3
from PyQt4.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt4.QtCore import Qt

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
        # set headers
        self.soloParticipantModel.setHeaderData(0, Qt.Horizontal, "First")
        self.soloParticipantModel.setHeaderData(1, Qt.Horizontal, "Last")
        self.soloParticipantModel.setHeaderData(2, Qt.Horizontal, "Address")
        self.soloParticipantModel.setHeaderData(3, Qt.Horizontal, "Town")
        self.soloParticipantModel.setHeaderData(4, Qt.Horizontal, "Postal Code")
        self.soloParticipantModel.setHeaderData(5, Qt.Horizontal, "Home Phone")
        self.soloParticipantModel.setHeaderData(6, Qt.Horizontal, "Cell Phone")
        self.soloParticipantModel.setHeaderData(7, Qt.Horizontal, "Email")
        self.soloParticipantModel.setHeaderData(8, Qt.Horizontal, "Date of Birth")
        self.soloParticipantModel.setHeaderData(10, Qt.Horizontal, "School Attending")
        self.soloParticipantModel.setHeaderData(11, Qt.Horizontal, "Parent")
        self.soloParticipantModel.setHeaderData(12, Qt.Horizontal, "Age")
        self.soloParticipantModel.setHeaderData(13, Qt.Horizontal, "School Grade")

        # GroupParticipant
        self.groupParticipantModel = QSqlTableModel(db=self.conn)
        self.groupParticipantModel.setTable("groupparticipants")
        self.groupParticipantModel.select()
        # set headers
        self.groupParticipantModel.setHeaderData(1, Qt.Horizontal, "Group Name")
        self.groupParticipantModel.setHeaderData(2, Qt.Horizontal, "Group Size")
        self.groupParticipantModel.setHeaderData(3, Qt.Horizontal, "School Grade")
        self.groupParticipantModel.setHeaderData(4, Qt.Horizontal, "Average Age")
        self.groupParticipantModel.setHeaderData(5, Qt.Horizontal, "Participants")
        self.groupParticipantModel.setHeaderData(6, Qt.Horizontal, "Contact")
        self.groupParticipantModel.setHeaderData(7, Qt.Horizontal, "Earliest Performance Time")
        self.groupParticipantModel.setHeaderData(8, Qt.Horizontal, "Latest Performance Time")

        # Teacher
        self.teacherModel = QSqlTableModel(db=self.conn)
        self.teacherModel.setTable("teachers")
        self.teacherModel.select()
        # set headers
        self.teacherModel.setHeaderData(1, Qt.Horizontal, "First")
        self.teacherModel.setHeaderData(2, Qt.Horizontal, "Last")
        self.teacherModel.setHeaderData(3, Qt.Horizontal, "Address")
        self.teacherModel.setHeaderData(4, Qt.Horizontal, "Town")
        self.teacherModel.setHeaderData(5, Qt.Horizontal, "Postal Code")
        self.teacherModel.setHeaderData(6, Qt.Horizontal, "Daytime Phone")
        self.teacherModel.setHeaderData(7, Qt.Horizontal, "Evening Phone")
        self.teacherModel.setHeaderData(8, Qt.Horizontal, "Email")

        # Entry
        self.entryModel = QSqlTableModel(db=self.conn)
        self.entryModel.setTable("entries")
        self.entryModel.select()
        # set headers
        self.entryModel.setHeaderData(1, Qt.Horizontal, "Participant")
        self.entryModel.setHeaderData(2, Qt.Horizontal, "Teacher")
        self.entryModel.setHeaderData(3, Qt.Horizontal, "Discipline")
        self.entryModel.setHeaderData(4, Qt.Horizontal, "Level")
        self.entryModel.setHeaderData(5, Qt.Horizontal, "Class Number")
        self.entryModel.setHeaderData(6, Qt.Horizontal, "Class Name")
        self.entryModel.setHeaderData(7, Qt.Horizontal, "Instrument")
        self.entryModel.setHeaderData(8, Qt.Horizontal, "Years of Instruction")
        self.entryModel.setHeaderData(9, Qt.Horizontal, "Scheduling Requirements")

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
                (first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth, school_attending, parent, age, school_grade) \
                VALUES (:first, :last, :address, :town, :postal, :home, :cell, :email, :dob, :schoolAttending, :parent, :age, :schoolGrade)")
            query.bindValue(":first", sp.first)
            query.bindValue(":last", sp.last)
            query.bindValue(":address", sp.address)
            query.bindValue(":town", sp.town)
            query.bindValue(":postal", sp.postal)
            query.bindValue(":home", sp.home)
            query.bindValue(":cell", sp.cell)
            query.bindValue(":email", sp.email)
            query.bindValue(":dob", sp.dob)
            query.bindValue(":schoolAttending", sp.schoolAttending)
            query.bindValue(":parent", sp.parent)
            query.bindValue(":age", sp.age)
            query.bindValue(":schoolGrade", sp.schoolGrade)
            query.exec_()
            self.soloParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addSoloParticipant FAILED\n\tquery: {0}\n\terror: {1}".format(query, e)
            return e

    def updateSoloParticipant(self, participantId, participant):
        """Updates a SoloParticipant record"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE soloparticipants \
                SET first_name=:first, last_name=:last, address=:address, town=:town, postal_code=:postal,\
                home_phone=:home, cell_phone=:cell, email=:email, date_of_birth=:dob, school_attending=:schoolAttending, parent=:parent, age=:age, school_grade=:schoolGrade \
                WHERE id=:id")
            query.bindValue(":first", participant.first)
            query.bindValue(":last", participant.last)
            query.bindValue(":address", participant.address)
            query.bindValue(":town", participant.town)
            query.bindValue(":postal", participant.postal)
            query.bindValue(":home", participant.home)
            query.bindValue(":cell", participant.cell)
            query.bindValue(":email", participant.email)
            query.bindValue(":dob", participant.dob)
            query.bindValue(":schoolAttending", participant.schoolAttending)
            query.bindValue(":parent", participant.parent)
            query.bindValue(":age", participant.age)
            query.bindValue(":schoolGrade", participant.schoolGrade)
            query.bindValue(":id", participantId)
            query.exec_()
            self.soloParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "updateSoloParticipant FAILED\n\tquery: {0}\n\terror: {1}".format(query, e)
            return e

    def addGroupParticipant(self, gp):
        """Adds a new GroupParticipant record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO groupparticipants \
                (group_name, group_size, school_grade, average_age, participants, contact, earliest_performance_time, latest_performance_time) \
                VALUES (:groupName, :groupSize, :schoolGrade, :averageAge, :participants, :contact, :earliestPerformanceTime, :latestPerformanceTime)")
            query.bindValue(":groupName", gp.groupName)
            query.bindValue(":groupSize", gp.groupSize)
            query.bindValue(":schoolGrade", gp.schoolGrade)
            query.bindValue(":averageAge", gp.averageAge)
            query.bindValue(":participants", gp.participants)
            query.bindValue(":contact", gp.contact)
            query.bindValue(":earliestPerformanceTime", gp.earliestPerformanceTime)
            query.bindValue(":latestPerformanceTime", gp.latestPerformanceTime)
            query.exec_()
            self.groupParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addGroupParticipant FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def updateGroupParticipant(self, participantId, participant):
        """Updates GroupParticipant record"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE groupparticipants \
                SET group_name=:groupName, group_size=:groupSize, school_grade=:schoolGrade,\
                average_age=:averageAge, participants=:participants, contact=:contact, earliest_performance_time=:earliestPerformanceTime, latest_performance_time=:latestPerformanceTime \
                WHERE id=:id")
            query.bindValue(":groupName", participant.groupName)
            query.bindValue(":groupSize", participant.groupSize)
            query.bindValue(":schoolGrade", participant.schoolGrade)
            query.bindValue(":averageAge", participant.averageAge)
            query.bindValue(":participants", participant.participants)
            query.bindValue(":contact", participant.contact)
            query.bindValue(":earliestPerformanceTime", participant.earliestPerformanceTime)
            query.bindValue(":latestPerformanceTime", participant.latestPerformanceTime)
            query.bindValue(":id", participantId)
            query.exec_()
            self.groupParticipantModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "updateGroupParticipant FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
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

    def updateTeacher(self, teacherId, teacher):
        """Updates a Teacher record"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE teachers \
                SET first_name=:first, last_name=:last, address=:address, city=:city, postal_code=:postal,\
                daytime_phone=:daytimePhone, evening_phone=:eveningPhone, email=:email \
                WHERE id=:id")
            query.bindValue(":first", teacher.first)
            query.bindValue(":last", teacher.last)
            query.bindValue(":address", teacher.address)
            query.bindValue(":city", teacher.city)
            query.bindValue(":postal", teacher.postal)
            query.bindValue(":daytimePhone", teacher.daytimePhone)
            query.bindValue(":eveningPhone", teacher.eveningPhone)
            query.bindValue(":email", teacher.email)
            query.bindValue(":id", teacherId)
            query.exec_()
            self.teacherModel.select()
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "updateTeacher FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def addEntry(self, entry):
        """Adds a new Entry record to the db"""
        entryId = None
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO entries \
                (participant_id, teacher_id, discipline, level, class_number, class_name, instrument, years_of_instruction, scheduling_requirements) \
                VALUES (:participantID, :teacherID, :discipline, :level, :classNumber, :className, :instrument, :yearsOfInstruction, :schedulingRequirements)")
            query.bindValue(":participantID", entry.participantID)
            query.bindValue(":teacherID", entry.teacherID)
            query.bindValue(":discipline", entry.discipline)
            query.bindValue(":level", entry.level)
            query.bindValue(":classNumber", entry.classNumber)
            query.bindValue(":className", entry.className)
            query.bindValue(":instrument", entry.instrument)
            query.bindValue(":yearsOfInstruction", entry.yearsOfInstruction)
            query.bindValue(":schedulingRequirements", entry.schedulingRequirements)
            query.exec_()
            self.entryModel.select()
            # get id
            entryId = self.getLastEntryId()
            # add selections to db
            for selection in entry.selections:
                self.addSelection(selection, entryId)
            return ""
        except Exception, e:
            # If something went wrong adding the selections, we want to delete the whole entry
            if entryId != None:
                self.deleteEntryFromId(entryId)
            # TODO: log this instead of printing to console
            print "addEntry FAILED\n\tquery: {0}\n\terror: {1}".format(query.query.lastError().text(), e)
            return e

    def updateEntry(self, entryId, entry):
        """Updates an Entry record"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE entries \
                SET participant_id=:participantID, teacher_id=:teacherID, discipline=:discipline,\
                level=:level, class_number=:class_number, class_name=:class_name, instrument=:instrument, \
                years_of_instruction, scheduling_requirements) \
                WHERE id=:id")
            query.bindValue(":participantID", entry.participantID)
            query.bindValue(":teacherID", entry.teacherID)
            query.bindValue(":discipline", entry.discipline)
            query.bindValue(":level", entry.level)
            query.bindValue(":classNumber", entry.classNumber)
            query.bindValue(":className", entry.className)
            query.bindValue(":instrument", entry.instrument)
            query.bindValue(":yearsOfInstruction", entry.yearsOfInstruction)
            query.bindValue(":schedulingRequirements", entry.schedulingRequirements)
            query.bindValue(":id", entryId)
            query.exec_()
            self.entryModel.select()
            # delete all selections associated with this entry (handles deleting selections during update)
            self.deleteSelectionsFromEntryId(entryId)
            # re-add selections to db (handles updates and new selections)
            for selection in entry.selections:
                self.addSelection(selection, entryId)
            return ""
        except Exception, e:
            # If something went wrong adding the selections, we want to delete the whole entry
            if entryId != None:
                self.deleteEntryFromId(entryId)
            # TODO: log this instead of printing to console
            print "addEntry FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def addSelection(self, selection, entryId):
        """Adds a new Selection record to the db"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO selections \
                (title, performance_time, composer_arranger, entry_id, title_of_musical) \
                VALUES (:title, :performanceTime, :composerArranger, :entryId, :titleOfMusical)")
            query.bindValue(":title", selection['title'])
            query.bindValue(":performanceTime", selection['performanceTime'])
            query.bindValue(":composerArranger", selection['composerArranger'])
            query.bindValue(":entryId", entryId)
            query.bindValue(":titleOfMusical", selection['titleOfMusical'])
            query.exec_()
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addSelection FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def deleteSelectionsFromEntryId(self, entryId):
        """Deletes all selections that reference entryId"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM selections \
                WHERE entry_id=:id")
            query.bindValue(":id", entryId)
            query.exec_()
        except Exception, e:
            # TODO: log this instead of printing to console
            print "deleteSelectionsFromEntryId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e    

    #####

    def deleteEntryFromId(self, entryId):
        try:
            query = QSqlQuery(self.conn)
            # Delete the entry
            query.prepare("DELETE FROM entries WHERE id=:id")
            query.bindValue(":id", entryId)
            query.exec_()
            # Delete its selections
            query.prepare("DELETE FROM selections WHERE entry_id=:id")
            query.bindValue(":id", entryId)
            query.exec_()
            self.entryModel.select()
        except Exception, e:
            # TODO: log this instead of printing to console
            print "deleteEntryFromId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    #####

    def getParticipantFromId(self, participantId):
        """Retrieve the appropriate Participant from the given id"""
        try:
            query = QSqlQuery(self.conn)
            if participantId[0] == 's':
                query.prepare("SELECT first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth, school_attending, parent \
                    FROM soloparticipants WHERE id=:id")
            else:
                query.prepare("SELECT group_name, group_size, school_grade, average_age, participants, contact \
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
                schoolAttending = str(query.value(9).toString())
                parent = str(query.value(10).toString())
                retrievedParticipant = SoloParticipant(first, last, address, town, postal, home, cell, email, dob, schoolAttending, parent)
            else:
                groupName = str(query.value(0).toString())
                groupSize = str(query.value(1).toString())
                schoolGrade = str(query.value(2).toString())
                averageAge = str(query.value(3).toString())
                participants = str(query.value(4).toString())
                contact = str(query.value(5).toString())
                retrievedParticipant = GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants, contact)
            return retrievedParticipant
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getParticipantFromId FAILED\n\tquery: {0}\
                \n\terror: {1}".format(query.lastQuery(), e)

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

    def getSoloParticipantsWithName(self, first, last):
        """Looks for solo participants with the given name"""
        pList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT first_name, last_name, address, town, postal_code, home_phone, \
                cell_phone, email, date_of_birth, school_attending, parent \
                FROM soloparticipants WHERE first_name=:first AND last_name=:last")
            query.bindValue(":first", first)
            query.bindValue(":last", last)
            query.exec_()
            while query.next() == True:
                first = str(query.value(0).toString())
                last = str(query.value(1).toString())
                address = str(query.value(2).toString())
                town = str(query.value(3).toString())
                postal = str(query.value(4).toString())
                home = str(query.value(5).toString())
                cell = str(query.value(6).toString())
                email = str(query.value(7).toString())
                dob = str(query.value(8).toString())
                schoolAttending = str(query.value(9).toString())
                parent = str(query.value(10).toString())
                pList.append(SoloParticipant(first, last, address, town, postal, home, cell, email, dob, schoolAttending, parent))
            return pList
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

    def getGroupParticipantsWithName(self, name):
        """Looks for group participants with the given name"""
        pList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT group_name, group_size, school_grade, average_age, participants, contact \
                FROM groupparticipants WHERE group_name=:name")
            query.bindValue(':name', name)
            query.exec_()
            while query.next() == True:
                groupName = str(query.value(0).toString())
                groupSize = str(query.value(1).toString())
                schoolGrade = str(query.value(2).toString())
                averageAge = str(query.value(3).toString())
                participants = str(query.value(4).toString())
                contact = str(query.value(5).toString())
                pList.append(GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants, contact))
            return pList
        except Exception, e:
            raise e

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
            query.prepare("SELECT MAX(id) FROM teachers")
            query.exec_()
            query.next()
            teacherId = str(query.value(0).toString())
            return teacherId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastTeacherId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    def getLastEntryId(self):
        """Get the id of the most recently added Entry"""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT MAX(id) FROM entries")
            query.exec_()
            query.next()
            entryId = str(query.value(0).toString())
            return entryId
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getLastEntryId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    # def getLastPieceId(self):
    #     """Get the id of the most recently added Piece"""
    #     try:
    #         query = QSqlQuery(self.conn)
    #         query.prepare("SELECT seq FROM sqlite_sequence WHERE name='pieces'")
    #         query.next()
    #         pieceId = str(query.value(0).toString())
    #         return pieceId
    #     except Exception, e:
    #         # TODO: log this instead of printing to console
    #         print "getLastPieceId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)

    #####

    def getSelectionsFromEntryId(self, entryId):
        """Retrieves all the Selections associated with the entryId"""
        selectionList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT title, performance_time, composer_arranger, opus_no, movement \
                FROM selections WHERE entry_id=:id")
            query.bindValue(":id", entryId)
            query.exec_()
            while query.next() == True:
                fields = {}
                fields['title'] = str(query.value(0).toString())
                fields['performanceTime'] = str(query.value(1).toString())
                fields['composerArranger'] = str(query.value(2).toString())
                fields['opusNo'] = str(query.value(3).toString())
                fields['movement'] = str(query.value(4).toString())
                selectionList.append(fields)
            return selectionList
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getSelectionsFromEntryId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def getAllEntries(self):
        """Retrieve all the Entries and return them in a list"""
        entryList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT participant_id, teacher_id, discipline, level, class_number, \
                class_name, instrument, years_of_instruction, scheduling_requirements, id FROM entries")
            query.exec_()
            while query.next() == True:
                participantID = str(query.value(0).toString())
                teacherID = str(query.value(1).toString())
                discipline = str(query.value(2).toString())
                level = str(query.value(3).toString())
                classNumber = str(query.value(4).toString())
                className = str(query.value(5).toString())
                instrument = str(query.value(6).toString())
                yearsOfInstruction = str(query.value(7).toString())
                schedulingRequirements = str(query.value(8).toString())
                entryId = str(query.value(9).toString())
                # get associated selections
                selections = self.getSelectionsFromEntryId(entryId)
                ee = Entry(participantID, teacherID, discipline, level, yearsOfInstruction, classNumber, className, instrument, selections, schedulingRequirements)
                entryList.append(ee)
            return entryList
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getAllEntries FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def getEntryFromId(self, entryId):
        """Retrieve Entry from specified id."""
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT participant_id, teacher_id, discipline, level, class_number, \
                class_name, instrument, years_of_instruction, scheduling_requirements FROM entries \
                WHERE id=:id")
            query.bindValue(":id", entryId)
            query.exec_()
            query.next()
            participantID = str(query.value(0).toString())
            teacherID = str(query.value(1).toString())
            discipline = str(query.value(2).toString())
            level = str(query.value(3).toString())
            classNumber = str(query.value(4).toString())
            className = str(query.value(5).toString())
            instrument = str(query.value(6).toString())
            yearsOfInstruction = str(query.value(7).toString())
            schedulingRequirements = str(query.value(8).toString())
            entryId = str(query.value(9).toString())
            # get associated selections
            selections = self.getSelectionsFromEntryId(entryId)
            ee = Entry(participantID, teacherID, discipline, level, yearsOfInstruction, classNumber, className, instrument, selections, schedulingRequirements)
            return ee
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getEntryFromId FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

    def getAllEntriesInDiscipline(self, discipline):
        """Returns all the Entries for the given discipline"""
        entryList = []
        try:
            query = QSqlQuery(self.conn)
            query.prepare("SELECT participant_id, teacher_id, discipline, level, class_number, \
                class_name, instrument, years_of_instruction, scheduling_requirements, id FROM entries \
                WHERE discipline=:discipline")
            query.bindValue(":discipline", discipline)
            query.exec_()
            while query.next() == True:
                participantID = str(query.value(0).toString())
                teacherID = str(query.value(1).toString())
                discipline = str(query.value(2).toString())
                level = str(query.value(3).toString())
                classNumber = str(query.value(4).toString())
                className = str(query.value(5).toString())
                instrument = str(query.value(6).toString())
                yearsOfInstruction = str(query.value(7).toString())
                schedulingRequirements = str(query.value(8).toString())
                entryId = str(query.value(9).toString())
                # get associated selections
                selections = self.getSelectionsFromEntryId(entryId)
                ee = Entry(participantID, teacherID, discipline, level, yearsOfInstruction, classNumber, className, instrument, selections, schedulingRequirements)
                entryList.append(ee)
            return entryList
        except Exception, e:
            # TODO: log this instead of printing to console
            print "getAllEntriesInDiscipline FAILED\n\tquery: {0}\n\terror: {1}".format(query.lastQuery(), e)
            return e

# Global variable
dbInteractionInstance = DatabaseInteraction()
