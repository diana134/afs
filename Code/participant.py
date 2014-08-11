class Participant:
    """Holds participant data (name, address, contact info, etc) as strings"""
    def __init__(self, first=None, last=None, address=None, town=None, postal=None, home=None, cell=None, email=None, dob=None):
        self.first = str(first) if first is not None else None
        self.last = str(last) if last is not None else None
        self.address = str(address) if address is not None else None
        self.town = str(town) if town is not None else None
        self.postal = str(postal) if postal is not None else None
        self.home = str(home) if home is not None else None
        self.cell = str(cell) if cell is not None else None
        self.email = str(email) if email is not None else None
        self.dob = str(dob) if dob is not None else None

    def isEqualTo(self, obj):
        """check if obj is equal to this Participant"""
        if isinstance(obj, Participant):
            if (self.requiredFieldIsGood(self.first, obj.first) and
                    self.requiredFieldIsGood(self.last, obj.last) and
                    self.optionalFieldIsGood(self.address, obj.address) and
                    self.optionalFieldIsGood(self.town, obj.town) and
                    self.optionalFieldIsGood(self.postal, obj.postal) and
                    self.optionalFieldIsGood(self.home, obj.home) and
                    self.optionalFieldIsGood(self.cell, obj.cell) and
                    self.optionalFieldIsGood(self.email, obj.email) and
                    self.requiredFieldIsGood(self.dob, obj.dob)):
                return True
            else:
                return False
        else:
            return False

    def optionalFieldIsGood(self, mine, theirs):
        """check if optional field theirs matches with mine"""
        if (theirs is None or
                theirs == "" or
                theirs == mine):
            return True
        else:
            return False

    def requiredFieldIsGood(self, mine, theirs):
        """check if required field theirs matches with mine"""
        if (theirs is not None and
                mine == theirs):
            return True
        else:
            return False

    def addToDB(self, conn):
        """add this Participant to the database using connection conn"""
        conn.execute("INSERT INTO participants (first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.first, self.last, self.address, self.town, self.postal, self.home, self.cell, self.email, self.dob));
        conn.commit()
        return True