"""Deals with Teachers"""

from utilities import requiredFieldIsGood, optionalFieldIsGood

class Teacher(object):
    """Holds Teacher data (name, address, contact info, etc) as strings"""
    def __init__(self, first="", last="", address="", city="", postal="", daytimePhone="", eveningPhone="", email=""):
        # Deal with getting QStrings from UI
        # TODO: don't need to str anymore, handled at ui
        self.first = str(first) if first is not None else None
        self.last = str(last) if last is not None else None
        self.address = str(address) if address is not None else None
        self.city = str(city) if city is not None else None
        self.postal = str(postal) if postal is not None else None
        self.daytimePhone = str(daytimePhone) if daytimePhone is not None else None
        self.eveningPhone = str(eveningPhone) if eveningPhone is not None else None
        self.email = str(email) if email is not None else None
        
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
        # conn.execute("INSERT INTO teachers (first_name, last_name, address, city, postal_code, daytime_phone, evening_phone, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.first, self.last, self.address, self.city, self.postal, self.daytimePhone, self.eveningPhone, self.email));
        # conn.commit()
        # return True

        # Very important to send these in the correct order or shit breaks
        result = db.addTeacher((self.first, self.last, self.address, self.city, self.postal, self.daytimePhone, self.eveningPhone, self.email))
        return result
        
    def __str__(self):
        return '{0} {1}'.format(self.first,self.last)
