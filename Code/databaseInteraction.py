"""Handles all interactions with the database"""

import sys
import os
# import sqlite3
from PyQt4.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

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
        self.soloParticipantModel = QSqlTableModel()
        self.soloParticipantModel.setTable("soloparticipants")
        self.soloParticipantModel.select()

        # GroupParticipant
        self.groupParticipantModel = QSqlTableModel()
        self.groupParticipantModel.setTable("groupparticipants")
        self.groupParticipantModel.select()

    def close(self):
        """Clean everything up and close the connection"""
        self.conn.close()

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
            return ""
        except Exception, e:
            # TODO: log this instead of printing to console
            print "addSoloParticipant FAILED\n\tquery: {0}\
                \n\tvalues: {1}\n\terror: {2}".format(query, values, e)
            return e