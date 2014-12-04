"""Deals with Entries"""

from utilities import requiredFieldIsGood, optionalFieldIsGood

class Entry(object):
    """holds Entry data as strings"""
    def __init__(self, participantID="", teacherID="", discipline="", level="", classNumber="", className="", style="", instrument="", pieces=None):
        self.participantID = participantID
        self.teacherID = teacherID
        self.discipline = discipline
        self.level = level
        self.classNumber = classNumber
        self.className = className
        self.instrument = instrument
        self.style = style
        self.pieces = pieces if pieces is not None else []

    def isEqualTo(self, obj):
        """check if obj is equal to this Entry (test purposes only?)"""
        if isinstance(obj, Entry):
            if (requiredFieldIsGood(self.participantID, obj.participantID) and 
                    requiredFieldIsGood(self.teacherID, obj.teacherID) and
                    requiredFieldIsGood(self.discipline, obj.discipline) and
                    optionalFieldIsGood(self.level, obj.level) and
                    requiredFieldIsGood(self.classNumber, obj.classNumber) and
                    requiredFieldIsGood(self.className, obj.className) and
                    optionalFieldIsGood(self.style, obj.style) and
                    optionalFieldIsGood(self.instrument, obj.instrument)):
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        print "Entry has pieces {0}".format(self.pieces)        
        return self.participantID + self.teacherID + self.discipline + self.level + self.classNumber + self.className + self.style + self.instrument
        
    @staticmethod
    def getCsvHeader():
        """Returns a comma-separated string of column headers for use in a CSV file"""
        return '"Participant","Teacher","Discipline","Level","Title","Performance Time","Style","Composer","Opus","No.","Movement","Arranger","Artist","Instrument","Author"'
        
    def export(self, csvFile, depth=2):
        """Write this entry to a csv file, padded with <depth> empty columns as indentation. \
        csvFile must be an open file with write permissions."""
        # super hack
        from databaseInteraction import dbInteractionInstance
        
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
