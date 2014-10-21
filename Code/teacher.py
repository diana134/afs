"""Deals with Teachers"""

from utilities import requiredFieldIsGood, optionalFieldIsGood

class Teacher(object):
    """Holds Teacher data (name, address, contact info, etc) as strings"""
    def __init__(self, first="", last="", address="", city="", postal="", daytimePhone="", eveningPhone="", email=""):
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.postal = postal
        self.daytimePhone = daytimePhone
        self.eveningPhone = eveningPhone
        self.email = email
        
    def isEqualTo(self, obj):
        """check if obj is equal to this Teacher"""
        if isinstance(obj, Teacher):
            if (requiredFieldIsGood(self.first, obj.first) and 
                    requiredFieldIsGood(self.last, obj.last) and
                    optionalFieldIsGood(self.address, obj.address) and
                    optionalFieldIsGood(self.city, obj.city) and
                    optionalFieldIsGood(self.postal, obj.postal) and
                    optionalFieldIsGood(self.daytimePhone, obj.daytimePhone) and
                    optionalFieldIsGood(self.eveningPhone, obj.eveningPhone) and
                    requiredFieldIsGood(self.email, obj.email)):
                return True
            else:
                return False
        else:
            return False

    def addToDB(self, db):
        """add this Teacher to the database using DatabaseInteraction db, return the result (i.e. an error)"""

        # Very important to send these in the correct order or shit breaks
        result = db.addTeacher((self.first, self.last, self.address, self.city, self.postal, self.daytimePhone, self.eveningPhone, self.email))
        return result
        
    def __str__(self):
        return '{0} {1}'.format(self.first, self.last)
