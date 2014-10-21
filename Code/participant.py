"""Deals with Participants"""

from utilities import requiredFieldIsGood, optionalFieldIsGood
from abc import ABCMeta, abstractmethod

class Participant(object):
    """Super class to hopefully make organizing things easier later"""
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def isEqualTo(self, obj):
        """check if obj is equal to this Participant"""
        pass

    @abstractmethod
    def addToDB(self, conn):
        """add this thing to the database"""
        pass

class SoloParticipant(Participant):
    """Holds participant data (name, address, contact info, etc) as strings"""
    def __init__(self, first="", last="", address="", town="", postal="", home="", cell="", email="", dob=""):
        self.first = first
        self.last = last
        self.address = address
        self.town = town
        self.postal = postal
        self.home = home
        self.cell = cell
        self.email = email
        self.dob = dob

    def isEqualTo(self, obj):
        """check if obj is equal to this SoloParticipant"""
        if isinstance(obj, SoloParticipant):
            if (requiredFieldIsGood(self.first, obj.first) and
                    requiredFieldIsGood(self.last, obj.last) and
                    optionalFieldIsGood(self.address, obj.address) and
                    optionalFieldIsGood(self.town, obj.town) and
                    optionalFieldIsGood(self.postal, obj.postal) and
                    optionalFieldIsGood(self.home, obj.home) and
                    optionalFieldIsGood(self.cell, obj.cell) and
                    optionalFieldIsGood(self.email, obj.email) and
                    requiredFieldIsGood(self.dob, obj.dob)):
                return True
            else:
                return False
        else:
            return False

    def addToDB(self, db):
        """add this SoloParticipant to the database using DatabaseInteraction db, return the result (i.e. an error)"""

        # Very important to send these in the correct order or shit breaks
        result = db.addSoloParticipant((self.first, self.last, self.address, self.town, self.postal, self.home, self.cell, self.email, self.dob))
        return result

    def __str__(self):
        return '{0} {1}'.format(self.first,self.last)


class GroupParticipant(Participant):
    """Holds GroupParticipant data (name, size, age, etc) as strings"""
    def __init__(self, groupName="", groupSize="", schoolGrade="", averageAge="", participants=""):
        self.groupName = groupName
        self.groupSize = groupSize
        self.schoolGrade = schoolGrade
        self.averageAge = averageAge
        self.participants = participants

    def isEqualTo(self, obj):
        """check if obj is equal to this GroupParticipant"""
        if isinstance(obj, GroupParticipant):
            if (requiredFieldIsGood(self.groupName, obj.groupName) and
                    optionalFieldIsGood(self.groupSize, obj.groupSize) and
                    optionalFieldIsGood(self.schoolGrade, obj.schoolGrade) and
                    optionalFieldIsGood(self.averageAge, obj.averageAge) and
                    optionalFieldIsGood(self.participants, obj.participants)):
                return True
            else:
                return False
        else:
            return False
        
    def addToDB(self, db):
        """add this SoloParticipant to the database using DatabaseInteraction db, return the result (i.e. an error)"""

        # Very important to send these in the correct order or shit breaks
        result = db.addGroupParticipant((self.groupName, self.groupSize, self.schoolGrade, self.averageAge, self.participants))
        return result

    def __str__(self):
        return self.groupName
