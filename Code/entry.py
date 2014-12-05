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
        return '"Participant","Teacher","Discipline","Level","Title","Style","Instrument","Time","Composer","Opus","No.","Movement","Arranger","Artist","Author"'
        
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
            
        s = '{indent}"{participantName}","{teacherName}","{discipline}","{level}","{title}","{style}","{instrument}","{pieces}",'.format(
            indent=leadingCommas,
            participantName=participant,
            teacherName=teacher,
            discipline=self.discipline,
            level=self.level,
            title=self.title,
            style=self.style,
            instrument=self.instrument)
        )
        
        # instead of duplicating all the entry data just have an indented list of all pieces
        for i in range(len(self.pieces)):
            if i!=0:
                s.append('{indent},,,,,,,,'.format(indent=leadingComas))
                
            s.append('"{time}","{composer}","{opus}","{no}","{movement}","{arranger}","{artist}","{author}"\n'.format(
                time=self.pieces[i]['time'],
                composer=self.pieces[i]['composer'],
                opus=self.pieces[i]['opus'],
                no=self.pieces[i]['no'],
                movement=self.pieces[i]['movement'],
                arranger=self.pieces[i]['arranger'],
                artist=self.pieces[i]['artist'],
                author=self.pieces[i]['author']
            ))
        
        csvFile.write(s)
