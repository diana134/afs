class Participant:
	"""Holds participant data (name, address, contact info, etc)"""
	def __init__(self, first=None, last=None, address=None, town=None, postal=None, home=None, cell=None, email=None, dob=None):
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
		if type(Participant):
			if (self.first == obj.first and
					self.last == obj.last and
					(obj.address is None or obj.address == "" or self.address == obj.address) and
					(obj.town is None or obj.town == "" or self.town == obj.town) and
					(obj.postal is None or obj.postal == "" or self.postal == obj.postal) and
					(obj.home is None or obj.home == "" or self.home == obj.home) and
					(obj.cell is None or obj.cell == "" or self.cell == obj.cell) and
					(obj.email is None or obj.email == "" or self.email == obj.email) and
					self.dob == obj.dob):
				return True
		else:
			return False

	def addToDB(self, conn):
		conn.execute("INSERT INTO participants (first_name, last_name, address, town, postal_code, home_phone, cell_phone, email, date_of_birth) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.first, self.last, self.address, self.town, self.postal, self.home, self.cell, self.email, self.dob));