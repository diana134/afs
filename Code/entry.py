"""Deals with Entries"""

from utilities import requiredFieldIsGood, optionalFieldIsGood

class Entry(object):
    """holds Entry data as strings"""
    def __init__(self, participantID="", teacherID="", discipline="", level="", classNumber="", className="", title="", performanceTime="", style="", composer="", opus="", no="", movement="", arranger="", artist="", instrument="", author=""):
        self.participantID = participantID
        self.teacherID = teacherID
        self.discipline = discipline
        self.level = level
        self.classNumber = classNumber
        self.className = className
        self.title = title
        self.performanceTime = performanceTime
        self.style = style
        self.composer = composer
        self.opus = opus
        self.no = no
        self.movement = movement
        self.arranger = arranger
        self.artist = artist
        self.instrument = instrument
        self.author = author

    def isEqualTo(self, obj):
        """check if obj is equal to this Entry (test purposes only?)"""
        if isinstance(obj, Entry):
            if (requiredFieldIsGood(self.participantID, obj.participantID) and 
                    requiredFieldIsGood(self.teacherID, obj.teacherID) and
                    requiredFieldIsGood(self.discipline, obj.discipline) and
                    optionalFieldIsGood(self.level, obj.level) and
                    requiredFieldIsGood(self.classNumber, obj.classNumber) and
                    requiredFieldIsGood(self.className, obj.className) and
                    requiredFieldIsGood(self.title, obj.title) and
                    optionalFieldIsGood(self.performanceTime, obj.performanceTime) and
                    optionalFieldIsGood(self.style, obj.style) and
                    optionalFieldIsGood(self.composer, obj.composer) and
                    optionalFieldIsGood(self.opus, obj.opus) and
                    optionalFieldIsGood(self.no, obj.no) and
                    optionalFieldIsGood(self.movement, obj.movement) and
                    optionalFieldIsGood(self.arranger, obj.arranger) and
                    optionalFieldIsGood(self.artist, obj.artist) and
                    optionalFieldIsGood(self.instrument, obj.instrument) and
                    optionalFieldIsGood(self.author, obj.author)):
                return True
            else:
                return False
        else:
            return False

    # def addToDB(self):
    #     """add this Entry to the database using connection conn"""

    #     # Very important to send these in the correct order or shit breaks
    #     result = dbInteractionInstance.addEntry((self.participantID, self.teacherID, self.discipline, self.level, self.classNumber, self.className, self.title, self.performanceTime, self.style, self.composer, self.opus, self.no, self.movement, self.arranger, self.artist, self.instrument, self.author))
    #     return result

    def __str__(self):
        return self.participantID + self.teacherID + self.discipline + self.level + self.classNumber + self.className + self.title + self.performanceTime + self.style + self.composer + self.opus + self.no + self.movement + self.arranger + self.artist + self.instrument + self.author
        
    @staticmethod
    def getCsvHeader():
        """Returns a comma-separated string of column headers for use in a CSV file"""
        return '"Participant","Teacher","Discipline","Level","Title","Performance Time","Style","Composer","Opus","No.","Movement","Arranger","Artist","Instrument","Author"'
        
    def export(self, csvFile, depth=2):
        """Write this entry to a csv file, padded with <depth> empty columns as indentation. \
        csvFile must be an open file with write permissions."""
        
        participant = dbInteractionInstance.getParticipantFromId(self.participantID)
        teacher = dbInteractionInstance.getTeacherFromId(self.teacherID)
        
        leadingCommas = ''
        for _ in range(depth):
            leadingCommas = leadingCommas+','
            
        s = '{indent}"{participantName}","{teacherName}","{discipline}","{level}","{title}","{time}","{style}","{composer}","{opus}","{no}","{movement}","{arranger}","{artist}","{instrument}","{author}"\n'.format(
            indent=leadingCommas,
            participantName=participant,
            teacherName=teacher,
            discipline=self.discipline,
            level=self.level,
            title=self.title,
            time=self.performanceTime,
            style=self.style,
            composer=self.composer,
            opus=self.opus,
            no=self.no,
            movement=self.movement,
            arranger=self.arranger,
            artist=self.artist,
            instrument=self.instrument,
            author=self.author
        )
        csvFile.write(s)
